"""init

Revision ID: 4315aa986a0b
Revises: None
Create Date: 2015-07-12 10:38:08.298886

"""

# revision identifiers, used by Alembic.
revision = '4315aa986a0b'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('baseinfo', sa.Column('high52w', sa.Float(), nullable=True))
    op.add_column('baseinfo', sa.Column('low52w', sa.Float(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('baseinfo', 'low52w')
    op.drop_column('baseinfo', 'high52w')
    ### end Alembic commands ###
