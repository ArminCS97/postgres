"""Adding a new column score

Revision ID: 94b5150c1d4f
Revises: 3b41f3e98254
Create Date: 2020-12-28 22:29:25.559934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94b5150c1d4f'
down_revision = '3b41f3e98254'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parts', sa.Column('part_score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('parts', 'part_score')
    # ### end Alembic commands ###