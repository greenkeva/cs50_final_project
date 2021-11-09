import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

def error_occurred(message):
    return render_template("error.html", message=message)
    
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
    
def change_password(password):
    return render_template("update.html")