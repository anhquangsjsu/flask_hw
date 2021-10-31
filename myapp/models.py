from myapp import db

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True, index = True)
    rank = db.Column(db.Integer)
    isVisited = db.Column(db.Boolean)