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

    from . import db
    db.init_app(app)

    @app.route("/")
    def index():
        date=datetime.date.today()
        dbconn=db.get_db()
        cursor=dbconn.cursor()
        cursor.execute("select count(*) from list")
        ntasks=cursor.fetchone()[0]
        cursor.execute("select count(*) from list where deadline<= now()")
        noverdue=cursor.fetchone()[0]
        return render_template("index.html", ntasks=ntasks, noverdue=noverdue)

    return app