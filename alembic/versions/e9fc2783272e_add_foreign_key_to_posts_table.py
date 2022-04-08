"""add foreign key to posts table

Revision ID: e9fc2783272e
Revises: 2cd96820da08
Create Date: 2022-04-08 15:30:06.013314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9fc2783272e'
down_revision = '2cd96820da08'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('post_user_fk', source_table="posts", referent_table="users", local_cols = ['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
