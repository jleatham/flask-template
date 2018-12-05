from flask import Flask, render_template, flash, redirect, url_for, request
from config import Config
from forms import LoginForm, archWeekForm
from test import testFunction
from mySmartSheet import archSheet, ss_get_client, ss_get_sheet_parsed
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
#access_token = app.config['SS_ACCESS_TOKEN']

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
        flash('Login requested for user {}, remember_me={}, testResult={}, radioExample={}, selectExample={}'.format(
            form.username.data, form.remember_me.data,testResult,form.radioExample.data, form.selectExample.data))
        return redirect(url_for('index'))
    return render_template('login2.html', title='Sign In-2', form=form)

@app.route('/rendertest', methods=['GET','POST'])
def rendertest():
    #dynamically rendered form : https://stackoverflow.com/questions/39640024/create-dynamic-fields-in-wtform-in-flask
    #SmartSheet API calls
    ss_client = ss_get_client(app.config['SS_ACCESS_TOKEN'])
    EN_list = ss_get_sheet_parsed(ss_client,archSheet)
    #date,internal,category,bullet,bLink,subBullet1,sb1Link,subBullet2,sb2Link,subBullet3,sb3Link,subBullet4,sb4Link,subBullet5,sb5Link
    #prep forms to flash return to index for now
    now  = datetime.now()
    date = now.strftime("%d %b %Y")
    arch = "EN"
    form = archWeekForm(request.form)
    print('test comment')
    if request.method == 'POST' and form.validate():
        flash('Date: {},  \nArchitecture: {}, \ninternal: {}, \ncategory: {}, \nbullet: {}, \nbLink: {}, \nsubBullet1: {}, \nsb1Link: {}, \nsubBullet2: {}, \nsb2Link: {}, \nsubBullet3: {}, \nsb3Link: {}, \nsubBullet4: {}, \nsb4Link: {}, \nsubBullet5: {}, \nsb5Link: {}'.format(
            date, arch,form.internal.data, form.category.data, form.bullet.data, form.bLink.data,
            form.subBullet1.data, form.sb1Link.data, form.subBullet2.data, form.sb2Link.data,
            form.subBullet3.data, form.sb3Link.data, form.subBullet4.data, form.sb4Link.data,
            form.subBullet5.data, form.sb5Link.data))
        return redirect(url_for('index'))    
    return render_template('rendertest.html', title='Render Test', EN_list=EN_list, form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.debug = True
