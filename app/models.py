from app import db,login

from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

# Here we will create our User Class

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(120),index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post',backref="author",lazy="dynamic") # TODO Create relationship for Posts 

    def __repr__(self):
        return '<USER {}>'.format(self.email)

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<POST {}>'.format(self.body)

# TODO create login user loader when login route is created

@login.user_loader
def load_user(id):
    return User.query.get(int(id))