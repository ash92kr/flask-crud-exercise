"""empty message

Revision ID: 15cbcf1e7976
Revises: 
Create Date: 2019-02-08 00:38:26.806506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15cbcf1e7976'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
