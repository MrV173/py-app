"""cascade

Revision ID: 0385fa088498
Revises: 22125ae42720
Create Date: 2023-12-10 16:50:05.454498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0385fa088498'
down_revision = '22125ae42720'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint('mahasiswa_ibfk_2', type_='foreignkey')
        batch_op.drop_constraint('mahasiswa_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_satu'], ['id'], ondelete='CASCADE')
        batch_op.create_foreign_key(None, 'dosen', ['dosen_Dua'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mahasiswa', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('mahasiswa_ibfk_1', 'dosen', ['dosen_Dua'], ['id'])
        batch_op.create_foreign_key('mahasiswa_ibfk_2', 'dosen', ['dosen_satu'], ['id'])

    # ### end Alembic commands ###
