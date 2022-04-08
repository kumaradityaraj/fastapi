"""add content column  to post table

Revision ID: 60415a71cc9d
Revises: 9aea59f0471c
Create Date: 2022-04-08 15:19:26.977696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60415a71cc9d'
down_revision = '9aea59f0471c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
