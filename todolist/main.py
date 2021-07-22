import psycopg2
import sys
from flask import Flask, render_template, g
from flask import Blueprint
from . import db

bp=Blueprint("todolist", "todolist", url_prefix="/todolist")


@bp.route("/")
def index():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("select count(*) from list")
    ntasks=cursor.fetchone()[0]
    return render_template("main.html",ntasks=ntasks)

@bp.route("/tasks")
def task_list():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("select * from list")
    tasks=cursor.fetchall()
    return render_template("tasklist.html", tasks=tasks)

if __name__=="__main__":
    app.run()