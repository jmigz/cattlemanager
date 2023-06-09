"""cattle model fixed birth year

Revision ID: 6bf0fa03af39
Revises: 8a68ad277bf4
Create Date: 2023-06-08 10:00:46.250839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bf0fa03af39'
down_revision = '8a68ad277bf4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cattle', schema=None) as batch_op:
        batch_op.drop_column('birth_year')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cattle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('birth_year', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
