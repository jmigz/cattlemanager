"""Update Cattle model

Revision ID: 652e5c0cd54b
Revises: b17b5252d925
Create Date: 2023-06-06 22:59:50.626341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '652e5c0cd54b'
down_revision = 'b17b5252d925'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cattle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag_number', sa.String(length=20), nullable=True),
    sa.Column('breed', sa.String(length=255), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('sex', sa.String(length=10), nullable=True),
    sa.Column('health_status', sa.String(length=255), nullable=True),
    sa.Column('vaccinations', sa.String(length=255), nullable=True),
    sa.Column('breeding_history', sa.String(length=255), nullable=True),
    sa.Column('is_removed', sa.Boolean(), nullable=True),
    sa.Column('removal_reason', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tag_number')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cattle')
    # ### end Alembic commands ###
