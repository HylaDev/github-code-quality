"""empty message

Revision ID: 224fd8963462
Revises: 67c61eead8d2
Create Date: 2020-03-28 22:30:19.428692

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '224fd8963462'
down_revision = '67c61eead8d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('use_via_format_for_sender', sa.Boolean(), server_default='1', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'use_via_format_for_sender')
    # ### end Alembic commands ###
