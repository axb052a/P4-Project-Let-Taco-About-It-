"""empty message

Revision ID: a5805c5bd14a
Revises: 
Create Date: 2023-10-17 11:13:19.294909

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5805c5bd14a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('taco_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_favorites_taco_id_tacos'), 'tacos', ['taco_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_favorites_taco_id_tacos'), type_='foreignkey')
        batch_op.drop_column('taco_id')

    # ### end Alembic commands ###
