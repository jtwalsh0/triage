"""add_matrix_uuid_to_eval

Revision ID: 0bca1ba9706e
Revises: 38f37d013686
Create Date: 2019-02-05 13:19:50.172109

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0bca1ba9706e'
down_revision = '38f37d013686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('evaluations', sa.Column('matrix_uuid', sa.Text(), nullable=True), schema='test_results')
    op.create_foreign_key(None, 'evaluations', 'matrices', ['matrix_uuid'], ['matrix_uuid'], source_schema='test_results', referent_schema='model_metadata')
    op.add_column('evaluations', sa.Column('matrix_uuid', sa.Text(), nullable=True), schema='train_results')
    op.create_foreign_key(None, 'evaluations', 'matrices', ['matrix_uuid'], ['matrix_uuid'], source_schema='train_results', referent_schema='model_metadata')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'evaluations', schema='train_results', type_='foreignkey')
    op.drop_column('evaluations', 'matrix_uuid', schema='train_results')
    op.drop_constraint(None, 'evaluations', schema='test_results', type_='foreignkey')
    op.drop_column('evaluations', 'matrix_uuid', schema='test_results')
    # ### end Alembic commands ###
