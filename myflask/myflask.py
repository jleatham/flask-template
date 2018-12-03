from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from forms import LoginForm
from test import testFunction

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Person'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Flask Template', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        testResult = testFunction(form.testField)
        flash('Login requested for user {}, remember_me={}, testResult={}'.format(
            form.username.data, form.remember_me.data,testResult))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        testResult = testFunction(form.testField)
        flash('Login requested for user {}, remember_me={}, testResult={}'.format(
            form.username.data, form.remember_me.data,testResult))
        return redirect(url_for('index'))
    return render_template('login2.html', title='Sign In-2', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
