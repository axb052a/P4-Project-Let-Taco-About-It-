"""mdae changes

Revision ID: 2201e2537b5c
Revises: a5805c5bd14a
Create Date: 2023-10-17 12:09:52.578643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2201e2537b5c'
down_revision = 'a5805c5bd14a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('image', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('taco_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['taco_id'], ['tacos.id'], name='fk_favorite_taco_id_tacos'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_favorite_user_id_users'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
