"""Fixed relationship issues

Revision ID: a83ec4e2f861
Revises: dd739cdb4c6d
Create Date: 2024-10-08 18:53:28.582829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83ec4e2f861'
down_revision = 'dd739cdb4c6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('hero_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('power_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.alter_column('power_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('hero_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
