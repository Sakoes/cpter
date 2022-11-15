"""Initial table generation & setup

Revision ID: 39aad3184973
Revises: 
Create Date: 2022-11-15 10:35:31.692676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39aad3184973'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proef',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('xCor', sa.Float(), nullable=True),
    sa.Column('yCor', sa.Float(), nullable=True),
    sa.Column('zCor', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_proef_id'), 'proef', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_proef_id'), table_name='proef')
    op.drop_table('proef')
    # ### end Alembic commands ###
