#!/usr/bin/env python

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config.base import DEBUG, SECRET_KEY, SQLALCHEMY_DATABASE_URI


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), unique=True, nullable=False)
    desc = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<image: {}>'.format(self.name)


@app.route('/')
def homepage():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=DEBUG, use_reloader=True)
