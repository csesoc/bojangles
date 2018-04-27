from flask import render_template_string, request, render_template
import re
from . import app

@app.route('/')
def home():
    return render_template("home.html")
