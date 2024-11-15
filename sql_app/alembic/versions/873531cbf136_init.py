"""init

Revision ID: 873531cbf136
Revises: d093fbb8fac7
Create Date: 2024-11-15 14:19:59.863442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '873531cbf136'
down_revision: Union[str, None] = 'd093fbb8fac7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('titulo', sa.String(), nullable=True))
    op.drop_index('ix_items_title', table_name='items')
    op.create_index(op.f('ix_items_titulo'), 'items', ['titulo'], unique=False)
    op.drop_column('items', 'title')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('title', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_items_titulo'), table_name='items')
    op.create_index('ix_items_title', 'items', ['title'], unique=False)
    op.drop_column('items', 'titulo')
    # ### end Alembic commands ###