"""Add roles for user profile

Revision ID: 435daceeabf9
Revises: b8bfc90b56a2
Create Date: 2020-03-22 17:30:52.615474

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '435daceeabf9'
down_revision = 'b8bfc90b56a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('real_name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'real_name')
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'about')
    # ### end Alembic commands ###
