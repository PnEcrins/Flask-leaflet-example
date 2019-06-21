from .env import DB

class User(DB.Model):
    __tablename__ = "user"
    id = DB.Column(DB.Integer, primary_key=True)
    surname = DB.Column(DB.String(64), index=True)
    email = DB.Column(DB.String(120), index=True)
    name = DB.Column(DB.String(64), index=True)
    X = DB.Column(DB.Float)
    Y = DB.Column(DB.Float)

    def __repr__(self):
        return '<User {}>'.format(self.surname)
    
    def __repr__(self):
        return '<User {}>'.format(self.name)