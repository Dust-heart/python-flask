from flask import Blueprint

blue_print = Blueprint("blue_print", __name__)


@blue_print.route('/aaa')
def aa():
    return "aaa"


@blue_print.route('/bbb')
def bb():
    return "bbb"

