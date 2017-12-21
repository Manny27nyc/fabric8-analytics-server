"""Make ecosystem name unique.

Revision ID: 2ff043a5af5b
Revises: a46a17bfd29b
Create Date: 2016-08-04 10:21:47.217594

"""

# revision identifiers, used by Alembic.
revision = '2ff043a5af5b'
down_revision = 'a46a17bfd29b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    """Upgrade the database to a newer revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'ecosystems', ['name'])
    # end Alembic commands ###


def downgrade():
    """Downgrade the database to an older revision."""
    # commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ecosystems', type_='unique')
    # end Alembic commands ###
