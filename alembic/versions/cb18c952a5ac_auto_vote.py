"""auto-vote

Revision ID: cb18c952a5ac
Revises: 0dcdf7bdfa1f
Create Date: 2022-04-08 15:47:41.599905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb18c952a5ac'
down_revision = '0dcdf7bdfa1f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'],['posts_id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users_id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )
    pass


def downgrade():
    op.drop_table('votes')
    pass
