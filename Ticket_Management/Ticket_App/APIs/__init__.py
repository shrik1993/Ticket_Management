from flask import Blueprint

APIs = Blueprint('APIs', __name__)

from . import views