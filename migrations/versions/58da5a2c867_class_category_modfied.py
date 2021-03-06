"""class category modfied

Revision ID: 58da5a2c867
Revises: 9c67ce5048
Create Date: 2015-06-04 07:25:25.343011

"""

# revision identifiers, used by Alembic.
revision = '58da5a2c867'
down_revision = '9c67ce5048'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inv_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.drop_table('category')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='category_pkey'),
    sa.UniqueConstraint('name', name='category_name_key')
    )
    op.drop_table('inv_categories')
    ### end Alembic commands ###
