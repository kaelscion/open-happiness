from flask import render_template, flash, redirect, request
from app import app
import re

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/addstuff')
def add_stuff():
    return render_template('add_items.html')

@app.route('/dbAdd', methods=['GET', 'POST'])
def dbAdd():
    from app import db, models

    adj = request.form['adjAdd']
    split_adj = re.split('(?<!\d)[,.](?!\d)', adj)
    for item in split_adj:
        a = models.Adjectives(adjective=item)
        db.session.add(a)
    pos = request.form['posAdd']
    split_pos = re.split('(?<!\d)[,.](?!\d)', pos)
    for item in split_pos:
        p = models.Positive(category=item)
        db.session.add(p)
    db.session.commit()
    return "Database updated successfully!"
