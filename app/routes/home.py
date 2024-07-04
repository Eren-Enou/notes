from flask import Blueprint, render_template
from ..models import db
from ..models.note import Note

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def home():
    notes = Note.query.all()
    return render_template('home.html', notes=notes)
