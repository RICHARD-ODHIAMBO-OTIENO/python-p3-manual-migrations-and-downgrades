"""Renaming students to scholars

Revision ID: b66e6beca7c1
Revises: 
Create Date: 2024-07-21 14:17:05.744331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b66e6beca7c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
