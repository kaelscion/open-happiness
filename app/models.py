from app import db

class Adjectives(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    adjective = db.Column(db.String(250), index=True, nullable=False)

class Positive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(250), index=True, nullable=False)
