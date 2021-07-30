"""Rename password field in User model

Revision ID: eca124babf00
Revises: e8079c0a1146
Create Date: 2021-07-30 14:46:09.448478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eca124babf00'
down_revision = 'e8079c0a1146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.String(), nullable=True))
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###