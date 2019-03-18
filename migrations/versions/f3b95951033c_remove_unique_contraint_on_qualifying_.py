"""Remove unique contraint on Qualifying_Answer.user_session

Revision ID: f3b95951033c
Revises: 9f02092798e8
Create Date: 2019-03-17 21:14:17.550906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3b95951033c'
down_revision = '9f02092798e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_qualifying__answers_user_session', table_name='qualifying__answers')
    op.create_index(op.f('ix_qualifying__answers_user_session'), 'qualifying__answers', ['user_session'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_qualifying__answers_user_session'), table_name='qualifying__answers')
    op.create_index('ix_qualifying__answers_user_session', 'qualifying__answers', ['user_session'], unique=1)
    # ### end Alembic commands ###
