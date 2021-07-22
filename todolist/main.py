import psycopg2
import datetime
from flask import Flask, render_template, g, request,redirect, url_for
from flask import Blueprint
from . import db

bp=Blueprint("todolist", "todolist", url_prefix="/todolist")


@bp.route("/addtask", methods=["GET", "POST"])
def add_task():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    date=datetime.datetime.now().strftime('%Y-%m-%d')
    if request.method=="GET":
        return render_template("addtask.html",date=date)
    elif request.method=="POST":
        new_task=request.form.get("new_task")
        cursor.execute("insert into list (td_text) values (%s)",(new_task,))
        dbconn.commit()
        return redirect(url_for("todolist.task_list"),302)

@bp.route("/tasks")
def task_list():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("select * from list")
    tasks=cursor.fetchall()
    date=datetime.datetime.now().strftime('%Y-%m-%d')
    return render_template("tasklist.html", tasks=tasks, date=date)

if __name__=="__main__":
    app.run()