from flask import Flask, render_template
import datetime

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
        return render_template("index.html", date=date)

    return app