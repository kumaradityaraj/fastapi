"""create posts table

Revision ID: 9aea59f0471c
Revises: 
Create Date: 2022-04-08 15:11:47.298409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aea59f0471c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable = False, primary_key = True), sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
