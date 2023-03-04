"""Agregue tabla maestros

Revision ID: 6ed7f0b0784e
Revises: 99fabd4c0630
Create Date: 2023-03-03 20:58:57.793929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ed7f0b0784e'
down_revision = '99fabd4c0630'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('maestros',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.Text(), nullable=False),
    sa.Column('apellidos', sa.Text(), nullable=True),
    sa.Column('correo', sa.Text(), nullable=False),
    sa.Column('direccion', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('correo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('maestros')
    # ### end Alembic commands ###
