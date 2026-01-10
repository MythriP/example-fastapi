"""add content column to posts table

Revision ID: 4c221182c1e5
Revises: b8766bc770fc
Create Date: 2025-11-23 15:38:24.966130

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c221182c1e5'
down_revision: Union[str, Sequence[str], None] = 'b8766bc770fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))   
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
