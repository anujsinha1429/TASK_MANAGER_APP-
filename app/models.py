from app import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)
    task =db.relationship('Task',backref='owner',lazy=True)
class Task (db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(20))
    status=db.Column(db.String(20),default="not_started")
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)