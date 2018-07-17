from flask import Flask, request, redirect, render_template
from  flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://build-a-blog:hellothere@localhost/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    body = db.Column(db.String(250))
 
    def __init__(self, title, body):
        self.title = title
        self.body = body

# @app.route("/",methods=["POST"])
@app.route("/")
def index():
    # Create list of Blogs to be displayed on main page.
    blog_list = Blog.query.all()

    print(blog_list)

    return render_template('blog.html', blog_list=blog_list)

if __name__ == '__main__':
    app.run()

