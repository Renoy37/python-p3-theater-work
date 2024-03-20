"""Create Audition and Role Tables

Revision ID: fa53aa1c03ad
Revises: 
Create Date: 2024-03-20 12:23:37.703526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa53aa1c03ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Create auditions table
    op.create_table('auditions',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('actor', sa.String(), nullable=True),
                    sa.Column('location', sa.String(), nullable=True),
                    sa.Column('phone', sa.String(), nullable=True),
                    sa.Column('hired', sa.Boolean(), nullable=True),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )

    # Create roles table
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('character_name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    # Drop roles table
    op.drop_table('roles')

    # Drop auditions table
    op.drop_table('auditions')
