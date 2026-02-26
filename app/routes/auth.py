from flask import Blueprint,render_template,request,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from app import db
from app.models import User
from flask_login import login_user ,login_required,logout_user

auth=Blueprint('auth',__name__)

@auth.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        existing_user=User.query.filter_by(username=username).first()
        if existing_user:
            return "user already exist"
        hashed_password=generate_password_hash(password)

        new_user=User(username=username,password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    
    return render_template("register.html")


@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if not username or not password:
            return "username and passsword required"
        user=User.query.filter_by(username=username).first()

        if user is None:
            return "Invalid username or password "
        if not check_password_hash(user.password,password):
             return "incorrect password"
        
        login_user(user)
        return redirect(url_for("task.dashboard"))
           
    return render_template("login.html")

@auth.route("/logout",methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

