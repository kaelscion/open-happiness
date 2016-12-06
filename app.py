import os
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('main.html')

host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', '8080'))
app.run(host=host, port=port, debug=True)