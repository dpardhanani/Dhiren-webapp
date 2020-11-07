from app import app
from flask import render_template, request, redirect, url_for, session
import sqlite3 as sql

@app.route("/")
def redirect_home():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/create/task")
def create_task():
    return render_template("create_task.html")


@app.route("/add/task", methods=["POST", "GET"])
def add_task():
    print("adding task", request.method)
    con = ""
    if request.method == "POST":
        try:
            task_name = request.form["task_name"]
            priority = request.form["priority"]
            username = session.get("username")
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO To_do_list (task_name,priority,username) VALUES (?,?,?)", (task_name, priority, username))
                con.commit()
        except:
            con.rollback()
            msg = "Operation unsuccesful¢¢¢¢¢¢¢¢¢¢¢¢¢"
            return render_template("control_panel.html", msg=msg)
        finally:
            con.close()
            msg = "Operation succesful¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢"
            return render_template("control_panel.html", msg=msg)


@app.route("/show/list")
def view_list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from To_do_list order by Priority")
    rows = cur.fetchall()
    return render_template("show_list.html", rows=rows)


@app.route("/delete/task")
def delete_task():
    id = request.args.get("id")
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("delete from To_do_list where id = ?", id)
    con.commit()
    msg = "Operation succesful¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢"
    return render_template("control_panel.html", msg=msg)


@app.route("/complete/task")
def complete_task():
    id = request.args.get("id")
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("delete from To_do_list where id = ?", id)
    con.commit()
    msg = "Operation succesful¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢"
    return render_template("control_panel.html", msg=msg)
