#!/usr/bin/env python -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request, g
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import db
from app.category import bp
from app.models import Source, Software, Tag, Category

@bp.route('/covidfonte', methods=['GET', 'POST'])
def Covid19_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Corona Vírus',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Covid19_Source.html',
        title=(_('Corona Vírus')), sources=sources)

@bp.route('/covidaplicacao', methods=['GET', 'POST'])
def Covid19_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Corona Vírus',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Covid19_Software.html',
        title=(_('Corona Vírus')), softwares=softwares)

@bp.route('/saudefonte', methods=['GET', 'POST'])
def Health_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Saúde',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Health_Source.html',
        title=_('Saúde'), sources=sources)

@bp.route('/saudeaplicacao', methods=['GET', 'POST'])
def Health_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Saúde',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Health_Software.html',
        title=_('Saúde'), softwares=softwares)

@bp.route('/educacaofonte', methods=['GET', 'POST'])
def Education_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Educação',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Education_Source.html',
        title=_('Educação'), sources=sources)

@bp.route('/educacaoaplicacao', methods=['GET', 'POST'])
def Education_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Educação',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Education_Software.html',
        title=_('Educação'), softwares=softwares)

@bp.route('/cinemafonte', methods=['GET', 'POST'])
def MovieTheater_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Cinema',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/MovieTheater_Source.html',
        title=_('Cinema'), sources=sources)

@bp.route('/cinemaaplicacao', methods=['GET', 'POST'])
def MovieTheater_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Cinema',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/MovieTheater_Software.html',
        title=_('Cinema'), softwares=softwares)

@bp.route('/musicafonte', methods=['GET', 'POST'])
def Music_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Música',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Music_Source.html',
        title=_('Música'), sources=sources)

@bp.route('/musicaaplicacao', methods=['GET', 'POST'])
def Music_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Música',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Music_Software.html',
        title=_('Música'), softwares=softwares)

@bp.route('/tecnologiafonte', methods=['GET', 'POST'])
def Technology_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Tecnologia',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Technology_Source.html',
        title=_('Tecnologia'), sources=sources)

@bp.route('/tecnologiaaplicacao', methods=['GET', 'POST'])
def Technology_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Tecnologia',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Technology_Software.html',
        title=_('Tecnologia'), softwares=softwares)

@bp.route('/cienciafonte', methods=['GET', 'POST'])
def Science_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Ciência',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Science_Source.html',
        title=_('Ciência'), sources=sources)

@bp.route('/cienciaaplicacao', methods=['GET', 'POST'])
def Science_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Ciência',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Science_Software.html',
        title=_('Ciência'), softwares=softwares)

@bp.route('/segurancafonte', methods=['GET', 'POST'])
def PublicSecurity_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Segurança Pública',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/PublicSecurity_Source.html',
        title=_('Segurança Pública'), sources=sources)

@bp.route('/segurancaaplicacao', methods=['GET', 'POST'])
def PublicSecurity_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Segurança Pública',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/PublicSecurity_Software.html',
        title=_('Segurança Pública'), softwares=softwares)

@bp.route('/meioambientefonte', methods=['GET', 'POST'])
def Environment_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Meio Ambiente',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Environment_Source.html',
        title=_('Meio Ambiente'), sources=sources)

@bp.route('/meioambienteaplicacao', methods=['GET', 'POST'])
def Environment_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Meio Ambiente',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Environment_Software.html',
        title=_('Meio Ambiente'), softwares=softwares)

@bp.route('/culturafonte', methods=['GET', 'POST'])
def Culture_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Cultura',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Culture_Source.html',
        title=_('Cultura'), sources=sources)

@bp.route('/culturaaplicacao', methods=['GET', 'POST'])
def Culture_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Cultura',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Culture_Software.html',
        title=_('Cultura'), softwares=softwares)

@bp.route('/geografiafonte', methods=['GET', 'POST'])
def Geography_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Geografia',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Geography_Source.html',
        title=_('Geografia'), sources=sources)

@bp.route('/geografiaaplicacao', methods=['GET', 'POST'])
def Geography_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Geografia',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Geography_Software.html',
        title=_('Geografia'), softwares=softwares)

@bp.route('/financeirofonte', methods=['GET', 'POST'])
def Finances_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Finanças',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Finances_Source.html',
        title=_('Finanças'), sources=sources)

@bp.route('/financeiroaplicacao', methods=['GET', 'POST'])
def Finances_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Finanças',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Finances_Software.html',
        title=_('Finanças'), softwares=softwares)

@bp.route('/gastospublicosfonte', methods=['GET', 'POST'])
def PublicSpending_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Gastos Públicos',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/PublicSpending_Source.html',
        title=_('Gastos Públicos'), sources=sources)

@bp.route('/gastospublicosaplicacao', methods=['GET', 'POST'])
def PublicSpending_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Gastos Públicos',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/PublicSpending_Software.html',
        title=_('Gastos Públicos'), softwares=softwares)

@bp.route('/climafonte', methods=['GET', 'POST'])
def Climate_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Clima',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Climate_Source.html',
        title=_('Clima'), sources=sources)

@bp.route('/climaaplicacao', methods=['GET', 'POST'])
def Climate_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Clima',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Climate_Software.html',
        title=_('Clima'), softwares=softwares)

@bp.route('/esportelazerfonte', methods=['GET', 'POST'])
def Recreation_Source():
    sources = db.session.query(Source.title, Source.sphere, Category.category,
        Tag.keyword).filter(Category.category=='Esporte e Lazer',
        Category.source_id == Source.id, Source.tags).order_by(
        Source.timestamp.desc()).all()
    return render_template('category/Recreation_Source.html',
        title=_('Esporte e Lazer'), sources=sources)

@bp.route('/esportelazeraplicacao', methods=['GET', 'POST'])
def Recreation_Software():
    softwares = db.session.query(Software.title, Software.owner, Software.license,
        Category.category, Tag.keyword).filter(Category.category=='Esporte e Lazer',
        Category.software_id == Software.id, Software.tags).order_by(
        Software.timestamp.desc()).all()
    return render_template('category/Recreation_Software.html',
        title=_('Esporte e Lazer'), softwares=softwares)
