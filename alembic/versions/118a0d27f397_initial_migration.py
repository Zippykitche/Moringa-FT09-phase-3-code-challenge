"""Initial migration

Revision ID: 118a0d27f397
Revises: 
Create Date: 2024-12-15 11:12:59.599326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '118a0d27f397'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('magazines')
    op.drop_table('articles')
    op.alter_column('authors', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('authors', 'name',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('authors', 'name',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)
    op.alter_column('authors', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.create_table('articles',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('title', sa.TEXT(), nullable=False),
    sa.Column('content', sa.TEXT(), nullable=False),
    sa.Column('author_id', sa.INTEGER(), nullable=True),
    sa.Column('magazine_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.ForeignKeyConstraint(['magazine_id'], ['magazines.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('magazines',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('category', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
