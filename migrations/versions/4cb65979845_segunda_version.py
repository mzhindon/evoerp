"""segunda version

Revision ID: 4cb65979845
Revises: 58da5a2c867
Create Date: 2015-07-12 12:03:40.871743

"""

# revision identifiers, used by Alembic.
revision = '4cb65979845'
down_revision = '58da5a2c867'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cmn_brands',
    sa.Column('bnd_id', sa.Integer(), nullable=False),
    sa.Column('bnd_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('bnd_id'),
    sa.UniqueConstraint('bnd_name')
    )
    op.create_table('vhc_vehicle',
    sa.Column('veh_id', sa.Integer(), nullable=False),
    sa.Column('veh_model', sa.String(length=64), nullable=True),
    sa.Column('veh_type', sa.String(length=64), nullable=True),
    sa.Column('veh_version', sa.String(length=64), nullable=True),
    sa.Column('veh_manufacture_date_since', sa.Integer(), nullable=True),
    sa.Column('veh_manufacture_date_until', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('veh_id'),
    sa.UniqueConstraint('veh_model')
    )
    op.create_table('item',
    sa.Column('itm_id', sa.Integer(), nullable=False),
    sa.Column('itm_code', sa.String(length=64), nullable=True),
    sa.Column('itm_customs_code', sa.String(length=64), nullable=True),
    sa.Column('itm_quantity_on_hand', sa.Integer(), nullable=True),
    sa.Column('itm_quantity_on_order', sa.Integer(), nullable=True),
    sa.Column('itm_price', sa.Float(), nullable=True),
    sa.Column('itm_category_id_fk', sa.Integer(), nullable=True),
    sa.Column('itm_brand_id_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['itm_brand_id_fk'], ['cmn_brands.bnd_id'], ),
    sa.ForeignKeyConstraint(['itm_category_id_fk'], ['inv_categories.id'], ),
    sa.PrimaryKeyConstraint('itm_id'),
    sa.UniqueConstraint('itm_code'),
    sa.UniqueConstraint('itm_customs_code')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    op.drop_table('vhc_vehicle')
    op.drop_table('cmn_brands')
    ### end Alembic commands ###
