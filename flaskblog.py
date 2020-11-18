from flask import Flask, render_template, url_for, flash, redirect
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
def home():
    return render_template("home.html", posts = posts)


@app.route("/about")
def about():
    return render_template("about.html", title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@flask-blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful login. Please check username and password', 'danger')

    return render_template('login.html', title = 'Register', form = form)

if __name__  == '__main__':
    app.run(debug = True)