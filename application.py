import os
from flask import Flask, render_template, request

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import error_occurred, login_required


# create web server with flask, web app that listens for browser requests
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

USERS = ["ADMIN", "EMP"]
DEFAULT_PW = "HR_Right019"



# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///employee.db")
EMPLOYEES = db.execute("SELECT first_name, last_name, address, pay_rate FROM employees")


@app.route("/")
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_type = request.form.get("user_type")
        if not username:
            return error_occurred("Please enter username")
        elif not password:
            return error_occurred("Please enter password")
        elif not user_type:
            return error_occurred("Please enter ADMIN or EMP")
        user = db.execute("SELECT * FROM employees WHERE username = ?", username)
        if len(user) != 1 or not check_password_hash(user[0]["hash"], password):
            return error_occurred("Invalid username and/or password")
        session["user_id"] = user[0]["id"]
        if user_type == "ADMIN":
            return render_template("employees.html", EMPLOYEES=EMPLOYEES, pay=format(EMPLOYEES[0]["pay_rate"], ".2f"))
        if password == DEFAULT_PW:
            return render_template("update.html")
        return redirect("/")
    else:
        return render_template("login.html", USERS=USERS)


@app.route("/update", methods=["POST"])
@login_required
def change_password():
    if request.method == "POST":
        password = request.form.get("password")
        hash = generate_password_hash(password)
        print(password)
        db.execute("UPDATE employees SET hash = ? WHERE id = ?", hash, session["user_id"])
        return redirect("/login")
    else:
        return render_template("update.html")


@app.route("/logout")
def logout():
    # clear current user
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET","POST"])
@login_required
def register():
    if request.method == "POST":
        username = request.form.get("username")
        check_username = db.execute("SELECT username FROM employees WHERE username = ?", username)
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        address = request.form.get("address")
        pay = request.form.get("pay")
        user_type = request.form.get("user_type")
        if len(check_username) > 0:
            return error_occurred("username already exist")
        if not username:
            return error_occurred("Please enter username")
        elif not password:
            return error_occurred("Please enter password")
        elif not confirmation:
            return error_occurred("Please re-enter password")
        if password != confirmation:
            return error_occurred("Passwords must match")
        hash = generate_password_hash(password)
        db.execute("INSERT INTO employees (username, hash, first_name, last_name, address, pay_rate, user_type) VALUES (?, ?, ?, ?, ?, ?, ?)", username, hash, first_name, last_name, address, pay, user_type)
        return render_template("admin.html")
    else:
        return render_template("register.html", USERS=USERS)

@app.route("/profile")
@login_required
def profile():
    profile = db.execute("SELECT first_name, last_name, address, pay_rate FROM employees WHERE id = ?", session["user_id"])
    pay = format(profile[0]['pay_rate'], ".2f")
    return render_template("profile.html", profile=profile, pay=pay)

@app.route("/employees")
@login_required
def employees():
    pay = format(profile[0]['pay_rate'], ".2f")
    return render_template("employees.html", EMPLOYEES=EMPLOYEES, pay=pay)