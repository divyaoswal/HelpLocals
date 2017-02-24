"""empty message

Revision ID: 691cf7a01c25
Revises: 44c3c391fb5d
Create Date: 2017-02-23 17:38:02.946372

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '691cf7a01c25'
down_revision = '44c3c391fb5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contactName', sa.Text(), nullable=True),
    sa.Column('phoneNo', sa.Integer(), nullable=True),
    sa.Column('street', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###