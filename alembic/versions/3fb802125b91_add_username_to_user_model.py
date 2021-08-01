"""Add username to User model

Revision ID: 3fb802125b91
Revises: eca124babf00
Create Date: 2021-08-01 15:07:44.722871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fb802125b91'
down_revision = 'eca124babf00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
