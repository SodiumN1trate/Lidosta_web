"""empty message

Revision ID: 47d9fc1c7e33
Revises: 92e04034a682
Create Date: 2021-11-21 20:46:58.914948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47d9fc1c7e33'
down_revision = '92e04034a682'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_link', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.drop_column('image_link')

    op.create_table('sqlite_sequence',
    sa.Column('name', sa.NullType(), nullable=True),
    sa.Column('seq', sa.NullType(), nullable=True)
    )
    # ### end Alembic commands ###
