from flask import Blueprint

task= Blueprint('task',__name__)
@task.route("/")
def home():
    return "<h1> TO-DO Home page </h1>"