"""atualizei bd

Revision ID: bc8afcce886e
Revises: 42d8eb7e1f58
Create Date: 2020-10-26 23:09:18.879447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc8afcce886e'
down_revision = '42d8eb7e1f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('similar',
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('software_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['software_id'], ['software.id'], name=op.f('fk_similar_software_id_software')),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], name=op.f('fk_similar_source_id_source'))
    )
    op.create_table('tags',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('source_id', sa.Integer(), nullable=True),
    sa.Column('software_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['software_id'], ['software.id'], name=op.f('fk_tags_software_id_software')),
    sa.ForeignKeyConstraint(['source_id'], ['source.id'], name=op.f('fk_tags_source_id_source')),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], name=op.f('fk_tags_tag_id_tag'))
    )
    with op.batch_alter_table(u'tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('keyword', sa.String(length=500), nullable=True))
        batch_op.create_index(batch_op.f('ix_tag_keyword'), ['keyword'], unique=False)
        batch_op.drop_index('ix_tag_tag')
        batch_op.drop_constraint(u'fk_tag_source_id_source', type_='foreignkey')
        batch_op.drop_constraint(u'fk_tag_software_id_software', type_='foreignkey')
        batch_op.drop_column('source_id')
        batch_op.drop_column('software_id')
        batch_op.drop_column('tag')

    with op.batch_alter_table(u'user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', sa.Boolean(), nullable=True))
        batch_op.create_unique_constraint(batch_op.f('uq_user_nickname'), ['nickname'])
        batch_op.drop_index('ix_user_username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(u'user', schema=None) as batch_op:
        batch_op.create_index('ix_user_username', ['username'], unique=1)
        batch_op.drop_constraint(batch_op.f('uq_user_nickname'), type_='unique')
        batch_op.drop_column('confirmed')

    with op.batch_alter_table(u'tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', sa.VARCHAR(length=200), nullable=True))
        batch_op.add_column(sa.Column('software_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('source_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key(u'fk_tag_software_id_software', 'software', ['software_id'], ['id'])
        batch_op.create_foreign_key(u'fk_tag_source_id_source', 'source', ['source_id'], ['id'])
        batch_op.create_index('ix_tag_tag', ['tag'], unique=False)
        batch_op.drop_index(batch_op.f('ix_tag_keyword'))
        batch_op.drop_column('keyword')

    op.drop_table('tags')
    op.drop_table('similar')
    # ### end Alembic commands ###
