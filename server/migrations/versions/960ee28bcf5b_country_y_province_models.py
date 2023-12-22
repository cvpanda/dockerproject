"""country y province models

Revision ID: 960ee28bcf5b
Revises: aceea3baef57
Create Date: 2023-12-05 12:17:59.859402

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '960ee28bcf5b'
down_revision: Union[str, None] = 'aceea3baef57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('creator_id', sa.Integer(), nullable=False))
    op.add_column('event', sa.Column('timestamp', sa.DateTime(), nullable=False))
    op.add_column('event', sa.Column('date_and_time', sa.DateTime(), nullable=False))
    op.add_column('event', sa.Column('country_id', sa.Integer(), nullable=False))
    op.add_column('event', sa.Column('province_id', sa.Integer(), nullable=False))
    op.add_column('event', sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('event', sa.Column('price', sa.Float(), nullable=False))
    op.add_column('event', sa.Column('category_id', sa.Integer(), nullable=False))
    op.drop_index('ix_user_email', table_name='user')
    op.drop_table('localization')
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('province',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('province')
    op.drop_table('country')
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.drop_column('event', 'category_id')
    op.drop_column('event', 'price')
    op.drop_column('event', 'address')
    op.drop_column('event', 'province_id')
    op.drop_column('event', 'country_id')
    op.drop_column('event', 'date_and_time')
    op.drop_column('event', 'timestamp')
    op.drop_column('event', 'creator_id')
    # ### end Alembic commands ###
