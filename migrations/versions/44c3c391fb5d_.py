"""empty message

Revision ID: 44c3c391fb5d
Revises: 70d292c44a55
Create Date: 2017-02-23 14:59:09.592613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44c3c391fb5d'
down_revision = '70d292c44a55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('zipcode', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'zipcode')
    # ### end Alembic commands ###