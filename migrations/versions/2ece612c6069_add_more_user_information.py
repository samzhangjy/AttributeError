"""Add more user information

Revision ID: 2ece612c6069
Revises: 435daceeabf9
Create Date: 2020-03-23 10:24:21.699396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ece612c6069'
down_revision = '435daceeabf9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gender', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('site', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'site')
    op.drop_column('users', 'gender')
    # ### end Alembic commands ###
