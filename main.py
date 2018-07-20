from flask import Flask, request, redirect, render_template, flash
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

# Main 'home' page for Blogs...
@app.route("/blog")
def index():
    # Create list of Blogs to be displayed on main page.
    blog_list = Blog.query.all()
    print("Blog list=", blog_list)
    return render_template('blog.html', blog_list=blog_list)

# Input screen for a new Blog post...
@app.route("/newpost", methods=["POST","GET"])
def newpost():
    if request.method == 'POST':
        new_blog_title = request.form['new_blog_title']
        new_blog_entry = request.form['new_blog_entry']
        print(new_blog_entry, new_blog_title)

        # Create new BLog table record.
        blog = Blog(title=new_blog_title, body=new_blog_entry)
        db.session.add(blog)
        db.session.commit()

    return render_template('newpost.html')

# Process new Blog post...
@app.route("/newblog")
def newblog():
    return None

if __name__ == '__main__':
    app.run()

