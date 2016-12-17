from flask import render_template, flash, redirect, request
from app import app
import re

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/addstuff', methods=['GET', 'POST'])
def add_stuff():
    from app import db, models
    adj_query = models.Adjectives.query.all()
    pos_query = models.Positive.query.all()
    return render_template('add_items.html',
                            adjectives = adj_query,
                            positives = pos_query)


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
    flash("Database updated successfully!")
    return render_template('add_items.html')
