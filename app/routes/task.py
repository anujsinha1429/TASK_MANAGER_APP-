from flask import Blueprint,render_template,redirect,url_for,request,flash
from app import db  
from flask_login import login_required,current_user
from app.models import Task

task= Blueprint('task',__name__)
@task.route("/dashboard")
@login_required
def dashboard():
    tasks=Task.query.filter_by(user_id=current_user.id).all()
    return render_template("dashboard.html",tasks=tasks,page="dashboard")

@task.route("/add-task",methods=["POST"])
@login_required
def add_task():
    content= request.form.get("content")
    if not content:
        return redirect(url_for("task.dashboard"))
    new_task=Task(content=content,status="not_started",user_id=current_user.id)
    db.session.add(new_task)
    db.session.commit()
    flash("Task added successfully! ✅✅", "success")
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
    flash("Task deleted successfully! 🗑️", "danger")
    return redirect(url_for("task.taskboard"))

# @task.route("/toggle/<int:task_id>")
# @login_required
# def toggle_task(task_id):
#     task=Task.query.get_or_404(task_id)
#     #security check 
#     if task.user_id !=current_user.id:
#         return "you can not modify this task"
#     task.completed= not task.completed
#     db.session.commit()
#     return redirect(url_for("task.dashboard"))

@task.route("/status/<int:task_id>")
@login_required
def change_status(task_id):
    task=Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        return "you can not modify this task "
    elif task.status=="not_started":
        task.status="working"
        flash("task started!🚀", "info")
    elif task.status=="working":
        task.status="completed"
        flash("task completed!🎉", "success")
    else:
        task.status="not_started"
        flash("Task moved back to not started! 🔄", "warning")
    db.session.commit()
    return redirect(url_for("task.taskboard"))

@task.route("/taskboard")
@login_required
def taskboard():
    not_done=Task.query.filter_by(user_id=current_user.id,status="not_started").all()
    working= Task.query.filter_by(user_id=current_user.id,status="working").all()
    completed= Task.query.filter_by(user_id=current_user.id,status="completed").all()
    return render_template("taskboard.html",not_done=not_done,working=working,completed=completed,page="taskboard")

    