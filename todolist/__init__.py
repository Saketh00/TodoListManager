from flask import Flask, render_template
import datetime
import psycopg2

def create_app():
    app=Flask("todolist")

    app.config.from_mapping(
        DATABASE="todolist"
    )

    from . import main
    app.register_blueprint(main.bp)

    @app.route("/")
    def index():
        date=datetime.datetime.now().strftime('%Y-%m-%d')
        dbconn=db.get_db()
        cursor=dbconn.cursor()
        cursor.execute("select count(*) from list")
        ntasks=cursor.fetchone()[0]
        return render_template("index.html", date=date, ntasks=ntasks)

    return app