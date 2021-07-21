import psycopg2
import sys
from flask import Flask, render_template

app=Flask("Todolist site")

dbconn=psycopg2.connect("dbname=todolist")

@app.route("/")
def index():
    cursor=dbconn.cursor()
    cursor.execute("select count(*) from list")
    ntasks=cursor.fetchone()[0]
    return render_template("main.html",ntasks=ntasks)

@app.route("/tasks")
def task_list():
    cursor=dbconn.cursor()
    cursor.execute("select * from list")
    tasks=cursor.fetchall()
    return render_template("tasklist.html", tasks=tasks)

if __name__=="__main__":
    app.run()