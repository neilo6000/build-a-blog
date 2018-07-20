from flask import Flask, request, redirect, render_template
from  flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://build-a-blog:hellothere@localhost/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
 
    # id = db.Column(db.Integer, autoincrement=true, primary_key=True)
    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.serial, primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.String(250))
 
    def __init__(self, title, body):
        self.title = title
        self.body = body

        