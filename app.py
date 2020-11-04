from flask import Flask, render_template, jsonify
from postgres import Postgres

# sqlalchemy
connection = Postgres('postgres://jigsaw:secret@0.0.0.0:5432')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nhl')
def nhl():
    connection.run("INSERT INTO users VALUES ('homer simpson', 42)")
    users = connection.all('SELECT * FROM users;')
    return jsonify(users)

app.run(debug = True)

