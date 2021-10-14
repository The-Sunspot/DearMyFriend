
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from DearMyFriend import db

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(20))
    password=db.Column(db.String(128))

    def set_password(self,password):
        self.password=generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password,password)

class Word(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    text=db.Column(db.String(5000))
    author=db.Column(db.String(20),db.ForeignKey('user.id'))
