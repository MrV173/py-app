from app import db

class Gambar(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    path = db.Column(db.String(200), nullable=False)

def __repr__(self):
    return '<Gambar{}>'.format(self.name)