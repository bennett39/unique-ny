"""Add SubwayPoint geometry

Revision ID: 6c66fe5f2ad1
Revises: 47734b03d901
Create Date: 2022-08-06 14:45:40.230132

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision = '6c66fe5f2ad1'
down_revision = '47734b03d901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subwaystation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('geom', Geometry(geometry_type='POINT', srid=26918, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subwaystation')
    # ### end Alembic commands ###
