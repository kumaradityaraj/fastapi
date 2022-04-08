"""add phone number

Revision ID: 4c5ff7a35c76
Revises: cb18c952a5ac
Create Date: 2022-04-08 15:54:18.586794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c5ff7a35c76'
down_revision = 'cb18c952a5ac'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable = True))
    pass


def downgrade():
    op.drop_column('users','phone_number')
    pass
