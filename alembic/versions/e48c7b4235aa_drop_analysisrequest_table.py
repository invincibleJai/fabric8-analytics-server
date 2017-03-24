"""drop AnalysisRequest table

Revision ID: e48c7b4235aa
Revises: fc7ea2a7e386
Create Date: 2016-11-14 09:53:07.100233

"""

# revision identifiers, used by Alembic.
revision = 'e48c7b4235aa'
down_revision = 'fc7ea2a7e386'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analysis_requests')
    op.add_column('batches_versions', sa.Column('id', sa.Integer(), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('batches_versions', 'id')
    op.create_table('analysis_requests',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('job_id', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('submitted_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('fulfilled_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('analysis_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('version_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['analysis_id'], ['analyses.id'], name='analysis_requests_analysis_id_fkey'),
    sa.ForeignKeyConstraint(['version_id'], ['versions.id'], name='analysis_requests_version_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='analysis_requests_pkey')
    )
    ### end Alembic commands ###