from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from src.settings import db_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_config.build_connection_str()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(5), nullable=False)


db.create_all()

@app.route('/')
def root():
    return 'Hello World'

def get_random_word():
    pass