#!/usr/bin/env python -*- coding: utf-8 -*-
from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login
from app.search import add_to_index, remove_from_index, query_index


class SearchableMixin(object):
    @classmethod
    def search(cls, expression, page, per_page):
        ids, total = query_index(cls.__tablename__, expression, page, per_page)
        if total == 0:
            return cls.query.filter_by(id=0), 0
        when = []
        for i in range(len(ids)):
            when.append((ids[i], i))
        return cls.query.filter(cls.id.in_(ids)).order_by(
            db.case(when, value=cls.id)), total

    @classmethod
    def before_commit(cls, session):
        session._changes = {
            'add': list(session.new),
            'update': list(session.dirty),
            'delete': list(session.deleted)
        }

    @classmethod
    def after_commit(cls, session):
        for obj in session._changes['add']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['update']:
            if isinstance(obj, SearchableMixin):
                add_to_index(obj.__tablename__, obj)
        for obj in session._changes['delete']:
            if isinstance(obj, SearchableMixin):
                remove_from_index(obj.__tablename__, obj)
        session._changes = None

    @classmethod
    def reindex(cls):
        for obj in cls.query:
            add_to_index(cls.__tablename__, obj)

db.event.listen(db.session, 'before_commit', SearchableMixin.before_commit)
db.event.listen(db.session, 'after_commit', SearchableMixin.after_commit)


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(200), unique=True)
    username = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    about_me = db.Column(db.String(500))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed = db.Column(db.Boolean, nullable=True, default=False)
    sources = db.relationship('Source', backref='author', lazy='dynamic')
    softwares = db.relationship('Software', backref='author', lazy='dynamic')

    def __repr__(self):
        return '{}'.format(self.nickname)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.password_hash, senha)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode( {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    def get_confirm_register_token(self, expires_in=600):
        return jwt.encode( {'register_confirm': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    @staticmethod
    def verify_confirm_register_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'],
                            algorithms=['HS256'])['register_confirm']
        except:
            return
        return User.query.get(id)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))


similar = db.Table('similar',
    db.Column('source_id', db.Integer, db.ForeignKey('source.id')),
    db.Column('software_id', db.Integer, db.ForeignKey('software.id'))
)


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('source_id', db.Integer, db.ForeignKey('source.id')),
    db.Column('software_id', db.Integer, db.ForeignKey('software.id'))
)


class Source(SearchableMixin, db.Model):

    __searchable__ = ['title']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    sphere = db.Column(db.String(200), index=True)
    city = db.Column(db.String(200), index=True)
    state = db.Column(db.String(200), index=True)
    country = db.Column(db.String(200), index=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(300), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    similar = db.relationship('Software', secondary=similar,
        backref=db.backref('source_similar', lazy='dynamic'))
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('source_tag', lazy='dynamic'))
    categories = db.relationship('Category', backref='source_category', lazy='dynamic')
    comments = db.relationship('Comment', backref='source_comment', lazy='dynamic')
    reports = db.relationship('Report', backref='source_report', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{}'.format(self.title)

    def as_dict(self):
        return {
            'title': self.title,
            'sphere': self.sphere,
            'city': self.city,
            'state': self.state,
            'country': self.state,
            'description': self.description,
            'official_link': self.officialLink
        }


class Software(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(300), index=True)
    license = db.Column(db.String(200), index=True)
    owner = db.Column(db.String(200), index=True)
    dateCreation = db.Column(db.String(200), index=True, default=datetime.utcnow)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    similar = db.relationship('Software', secondary=similar,
        backref=db.backref('software_similar', lazy='dynamic'))
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('software_tag', lazy='dynamic'))
    categories = db.relationship('Category', backref='software_category', lazy='dynamic')
    comments = db.relationship('Comment', backref='software_comment', lazy='dynamic')
    reports = db.relationship('Report', backref='software_report', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '{}'.format(self.title)

    def as_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'official_link': self.officialLink,
            'license': self.license,
            'owner': self.owner,
            'date_creation': self.dateCreation
        }


class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(500), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '{}'.format(self.keyword)

    def as_dict(self):
        return {'keyword': self.keyword}


class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '{}'.format(self.category)


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), index=True)
    text = db.Column(db.String(600), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '{}'.format(self.username)


class Report(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    description = db.Column(db.String(500), index=True)
    type = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '{}'.format(self.name)
