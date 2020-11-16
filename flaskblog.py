from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f62efed8759d359688119ad62affe698'

posts = [
    {
        'author': 'Adrian Nowak',
        'title': 'Blog post 1',
        'content': 'First post contetn',
        'date_posted:': '10 November, 2020'
    },
    {
        'author': 'John Smith',
        'title': 'Blog Post 2',
        'content': "Content of the second post",
        'date_posted': '11 November, 2020'
    }

]

@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts = posts)


@app.route("/about")
def about():
    return render_template("about.html", title = 'About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Register', form = form)

if __name__  == '__main__':
    app.run(debug = True)