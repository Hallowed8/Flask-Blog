from flask import Flask, render_template

app = Flask(__name__)

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


if __name__  == '__main__':
    app.run(debug = True)