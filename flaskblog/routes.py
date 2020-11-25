from flask import render_template, url_for, flash, redirect, request
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'You account has been created! you are now able to Login', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            user = User.query.filter_by(email = form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                flash("You're now logged in.", 'success')
                return redirect(url_for('home'))
            else:
                flash('Unsuccessful login. Please check username and password', 'danger')

    return render_template('login.html', title = 'Register', form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You've been logged out", 'info')
    return redirect(url_for('home'))

@app.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', category= 'success')
        return redirect(url_for('account'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title = 'Account', image_file = image_file, form = form)