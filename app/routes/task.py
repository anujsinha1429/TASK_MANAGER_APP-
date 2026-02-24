from flask import Blueprint,render_template
from flask_login import login_required,current_user

task= Blueprint('task',__name__)
@task.route("/dashboard")
@login_required
def dashboard():
    return "<h1>welcome to the dashboard" + current_user.username +"</h1>"    