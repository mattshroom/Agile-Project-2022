"""results table

Revision ID: 678b0ec674ab
Revises: b1f4866e5248
Create Date: 2022-05-08 17:57:24.832328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '678b0ec674ab'
down_revision = 'b1f4866e5248'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logo',
    sa.Column('logo_id', sa.Integer(), nullable=False),
    sa.Column('logoname', sa.String(length=150), nullable=True),
    sa.Column('logolink', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('logo_id')
    )
    op.create_table('result',
    sa.Column('result_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('guesses', sa.Integer(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('logo_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['logo_id'], ['logo.logo_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('result_id')
    )
    op.create_index(op.f('ix_result_timestamp'), 'result', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_result_timestamp'), table_name='result')
    op.drop_table('result')
    op.drop_table('logo')
    # ### end Alembic commands ###
