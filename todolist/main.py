import psycopg2
from flask import Flask, render_template, g, request,redirect, url_for
from flask import Blueprint
from . import db

bp=Blueprint("todolist", "todolist", url_prefix="/todolist")


@bp.route("/addtask", methods=["GET", "POST"])
def add_task():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    if request.method=="GET":
        return render_template("addtask.html")
    elif request.method=="POST":
        new_task=request.form.get("new_task")
        input_date=request.form.get("input_date")
        cursor.execute("insert into list (td_text, deadline) values (%s,%s)",(new_task,input_date,))
        dbconn.commit()
        return redirect(url_for("todolist.task_list"),302)


@bp.route("/tasks")
def task_list():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("select * from list order by deadline asc")
    tasks=cursor.fetchall()
    return render_template("tasklist.html", tasks=tasks)

@bp.route("/weekschedule")
def week_schedule():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("select * from list where deadline >= now() and (deadline<= now()+interval '7 day') order by deadline asc")
    tasks=cursor.fetchall()
    return render_template("weektask.html", tasks=tasks)

@bp.route("/overdue")
def overdue_list():
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("select * from list where deadline<= now() order by deadline asc")
    tasks=cursor.fetchall()
    return render_template("overduetask.html", tasks=tasks)

@bp.route("/<value>/<tid>")
def delete_task(value,tid):
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("delete from list where id=(%s)",(tid,))
    dbconn.commit()
    if value=="all":
        return redirect(url_for("todolist.task_list"),302)
    elif value=="week":
        return redirect(url_for("todolist.week_schedule"), 302)
    elif value=="overdue":
        return redirect(url_for("todolist.overdue_list"), 302)

@bp.route("/<value>/<tid>/<status>")
def mark_task(value,tid,status):
    dbconn=db.get_db()
    cursor=dbconn.cursor()
    cursor.execute("update list set status = NOT status where id=(%s)",(tid,))
    dbconn.commit()
    if value=="all":
        return redirect(url_for("todolist.task_list"),302)
    elif value=="week":
        return redirect(url_for("todolist.week_schedule"), 302)
    elif value=="overdue":
        return redirect(url_for("todolist.overdue_list"), 302)


if __name__=="__main__":
    app.run()