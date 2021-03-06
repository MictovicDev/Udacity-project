"""empty message

Revision ID: 15cb1fded53f
Revises: faf3ebfbe667
Create Date: 2022-07-05 01:46:59.189487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15cb1fded53f'
down_revision = 'faf3ebfbe667'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_talent')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
