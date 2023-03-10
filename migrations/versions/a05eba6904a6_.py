"""empty message

Revision ID: a05eba6904a6
Revises: 150861201a92
Create Date: 2022-12-08 17:59:27.028248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a05eba6904a6'
down_revision = '150861201a92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kargo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kargoAdi', sa.String(), nullable=True),
    sa.Column('adet', sa.Integer(), nullable=True),
    sa.Column('yukseklik', sa.Integer(), nullable=True),
    sa.Column('genislik', sa.Integer(), nullable=True),
    sa.Column('kirilma', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kargo')
    # ### end Alembic commands ###
