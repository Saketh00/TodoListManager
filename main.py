import psycopg2
import sys

def task_list():
    dbconn=psycopg2.connect("dbname=todolist")
    cursor=dbconn.cursor()
    cursor.execute("select * from list")
    tasks=cursor.fetchall()
    for id,task in tasks:
        print(id, task)


def Insert():
    dbconn=psycopg2.connect("dbname=todolist")
    cursor=dbconn.cursor()
    f=open("insert.sql")
    sql_code=f.read()
    f.close()
    cursor.execute(sql_code)
    dbconn.commit()

def Create():
    dbconn=psycopg2.connect("dbname=todolist")
    cursor=dbconn.cursor()
    f=open("list.sql")
    sql_code=f.read()
    f.close()
    cursor.execute(sql_code)
    dbconn.commit()

def main(arg):
    if arg == "Create":
        Create()
    elif arg=="Insert":
        Insert()
    elif arg=="ListTask":
        task_list()
    else:
        print(f"Unknown command {arg}")

if __name__=="__main__":
    main(sys.argv[1])