from flask import render_template, request, redirect, url_for
from . import notes_bp
from ..models import db
from ..models.note import Note

@notes_bp.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('home_bp.home'))
    return render_template('notes/add_note.html')
