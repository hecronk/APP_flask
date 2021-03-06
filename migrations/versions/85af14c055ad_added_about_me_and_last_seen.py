"""added about me and last seen

Revision ID: 85af14c055ad
Revises: cdbe78f14071
Create Date: 2022-03-18 18:26:30.847734

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85af14c055ad'
down_revision = 'cdbe78f14071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
