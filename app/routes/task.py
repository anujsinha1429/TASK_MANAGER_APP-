from flask import Blueprint,render_template,redirect,url_for,request
from app import db  
from flask_login import login_required,current_user
from app.models import Task

task= Blueprint('task',__name__)
@task.route("/dashboard")
@login_required
def dashboard():
    tasks=Task.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html",tasks=tasks)

@task.route("/add-task",methods=["POST"])
@login_required
def add_task():
    content= request.form.get("content")
    if not content:
        return redirect(url_for("task.dashboard"))
    new_task=Task(content=content,user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for("task.dashboard"))

@task.route("/delete/<int:task_id>")
@login_required
def delete_task(task_id):
    task=Task.query.get_or_404(task_id)
    #security check to ensure that only the owner of the task can delete it
    if task.user_id != current_user.id:
        return " you can not delete this task"
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("task.dashboard"))