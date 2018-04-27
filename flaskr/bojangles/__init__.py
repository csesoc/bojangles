from flask import Blueprint

app = Blueprint(
    'bojangles',
    __name__,
    template_folder='templates',
    static_folder='static')

from . import views

