from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
login_manager=LoginManager() #in dono line seh abhi db bana nhi hai abhi bss remote control bana hai

def create_app(): # jb v flask app chahiye iss function ko call kro (application factory pattern)
    app=Flask(__name__)
    app.config['SECRET_KEY']='supersecretkey'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
    db.init_app(app)
    login_manager.init_app(app) #login system attach 
    login_manager.login_view="auth.login" # bina login ke dashboard khole toh login page redirect hojaiye 
    from app import models
    from app.routes.auth import auth
    from app.routes.task import task
    app.register_blueprint(auth)
    app.register_blueprint(task)
    return app
