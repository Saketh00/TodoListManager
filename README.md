# System Requirements
You should install and setup PostgreSQL.

# Introduction

The repository contains a web app which is a todo list manager. The following
features are supported

1. Adding a task.
1. Lists all the tasks.
1. Alerts overdue tasks when opened.
1. View weekly scheduled tasks.
1. can mark or unmark a task.


# Setting up

1. Open terminal and run command `createdb todolist` to create the database.  
1. Clone repository
1. Create a virtualenv and activate it
1. Install dependencies using `pip install -r requirements.txt`
1. `export FLASK_APP=todolist` to set the application
1. `flask initdb` to create the initial database
1. `flask run` to start the app.
