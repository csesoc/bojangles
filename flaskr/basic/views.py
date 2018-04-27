from flask import render_template_string, request, render_template
import re
from . import app

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/test')
def test():
    if re.match(r'[Cc]url.*',request.headers.get('User-Agent')):
        return render_template_string("you are curl")

    return render_template_string("hello")
