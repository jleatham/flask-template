from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from config import Config
from forms import LoginForm, archWeekForm, removeArchWeekForm
from test import testFunction
from myMarshmallow import Architecture, ArchitectureSchema
from mySmartSheet import access_token, archSheet, ss_get_client, ss_get_sheet_parsed, ss_update_row
from datetime import datetime
import json

app = Flask(__name__)
app.config.from_object(Config)
#access_token = app.config['SS_ACCESS_TOKEN']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Flask Template')

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
    #need to find a way to force this to update on each refresh
    ss_client = ss_get_client(access_token)
    EN_list = ss_get_sheet_parsed(ss_client,archSheet)
    #date,internal,category,bullet,bLink,subBullet1,sb1Link,subBullet2,sb2Link,subBullet3,sb3Link,subBullet4,sb4Link,subBullet5,sb5Link
    #prep forms to flash return to index for now
    now  = datetime.now()
    date = now.strftime("%d %b %Y")
    arch = "EN"
    form = archWeekForm(request.form)
    print('test comment')
    if request.method == 'POST' and form.validate():
        archObject = Architecture(date, arch, form.category.data, form.bullet.data, form.bLink.data,
            form.subBullet1.data, form.sb1Link.data, form.subBullet2.data, form.sb2Link.data,
            form.subBullet3.data, form.sb3Link.data, form.subBullet4.data, form.sb4Link.data,
            form.subBullet5.data, form.sb5Link.data, 12345678) #random row ID since we just post to bottom
        schema = ArchitectureSchema()
        archDict, errors = schema.dump(archObject) 
        rowAddResult = ss_update_row(ss_client,archSheet, archDict)
        if rowAddResult == 'SUCCESS':
            #need to pop this up as a modal and keep going on forms
            flash('Date: {},</br>  Architecture: {}, </br>category: {}, </br>bullet: {}, </br>bLink: {}, </br>subBullet1: {}, </br>sb1Link: {}, </br>subBullet2: {}, </br>sb2Link: {}, </br>subBullet3: {}, </br>sb3Link: {}, </br>subBullet4: {}, </br>sb4Link: {}, </br>subBullet5: {}, </br>sb5Link: {}'.format(
                date, arch, form.category.data, form.bullet.data, form.bLink.data,
                form.subBullet1.data, form.sb1Link.data, form.subBullet2.data, form.sb2Link.data,
                form.subBullet3.data, form.sb3Link.data, form.subBullet4.data, form.sb4Link.data,
                form.subBullet5.data, form.sb5Link.data))
            return redirect(url_for('index'))    
        else:
            flash('Error adding row')
            return redirect(url_for('index')) 
    return render_template('rendertest.html', title='Render Test', EN_list=EN_list, form=form)

@app.route('/rendertest2', methods=['GET'])
def rendertest2():
    #dynamically rendered form : https://stackoverflow.com/questions/39640024/create-dynamic-fields-in-wtform-in-flask
    #SmartSheet API calls
    #need to find a way to force this to update on each refresh
    ss_client = ss_get_client(access_token)
    EN_list = ss_get_sheet_parsed(ss_client,archSheet)
    #date,internal,category,bullet,bLink,subBullet1,sb1Link,subBullet2,sb2Link,subBullet3,sb3Link,subBullet4,sb4Link,subBullet5,sb5Link
    #prep forms to flash return to index for now

    addForm = archWeekForm()
    removeForm = removeArchWeekForm()
    removeForm.rowID.choices = [(x['rowID'],x['rowID']) for x in EN_list]   
    print('test comment')
    return render_template('rendertest2.html', title='Render Test', EN_list=EN_list, addForm=addForm, removeForm=removeForm)

@app.route('/addOld', methods=['POST'])
def addOld():
    ss_client = ss_get_client(access_token)
    
    addForm = archWeekForm()
    removeForm = removeArchWeekForm()
    if addForm.validate_on_submit():
        now  = datetime.now()
        date = now.strftime("%d %b %Y")
        arch = "EN"        
        print('made it to addForm validate')
        archObject = Architecture(date, arch, addForm.category.data, addForm.bullet.data, addForm.bLink.data,
            addForm.subBullet1.data, addForm.sb1Link.data, addForm.subBullet2.data, addForm.sb2Link.data,
            addForm.subBullet3.data, addForm.sb3Link.data, addForm.subBullet4.data, addForm.sb4Link.data,
            addForm.subBullet5.data, addForm.sb5Link.data, 12345678) #random row ID since we just post to bottom
        schema = ArchitectureSchema()
        archDict, errors = schema.dump(archObject) 
        rowAddResult = ss_update_row(ss_client,archSheet, archDict)    
    EN_list = ss_get_sheet_parsed(ss_client,archSheet)    
    return render_template('rendertest2.html',title='Render Test', EN_list=EN_list, addForm=addForm, removeForm=removeForm)

@app.route('/removeOld', methods=['POST'])
def removeOld():
    ss_client = ss_get_client(access_token)
    EN_list = ss_get_sheet_parsed(ss_client,archSheet) 
    addForm = archWeekForm()
    removeForm = removeArchWeekForm()
    removeForm.rowID.choices = [(x['rowID'],x['rowID']) for x in EN_list] 
    if removeForm.validate_on_submit():
        print('made it to form2 validate')
        print (removeForm.rowID.data)  
    EN_list = ss_get_sheet_parsed(ss_client,archSheet)   
    
    
                    
    return render_template('rendertest2.html', title='Render Test', EN_list=EN_list, addForm=addForm, removeForm=removeForm)



@app.route('/rendertest3', methods=['GET'])
def rendertest3():
    #dynamically rendered form : https://stackoverflow.com/questions/39640024/create-dynamic-fields-in-wtform-in-flask
    #SmartSheet API calls
    #need to find a way to force this to update on each refresh
    ss_client = ss_get_client(access_token)
    EN_list = ss_get_sheet_parsed(ss_client,archSheet)
    #date,internal,category,bullet,bLink,subBullet1,sb1Link,subBullet2,sb2Link,subBullet3,sb3Link,subBullet4,sb4Link,subBullet5,sb5Link
    #prep forms to flash return to index for now

    print('test comment')
    return render_template('rendertest3.html', title='Render Test', EN_list=EN_list)

@app.route('/rendertest4', methods=['GET'])
def rendertest4():
    #dynamically rendered form : https://stackoverflow.com/questions/39640024/create-dynamic-fields-in-wtform-in-flask
    #SmartSheet API calls
    #need to find a way to force this to update on each refresh
    ss_client = ss_get_client(access_token)
    archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect='EN')
    #date,internal,category,bullet,bLink,subBullet1,sb1Link,subBullet2,sb2Link,subBullet3,sb3Link,subBullet4,sb4Link,subBullet5,sb5Link
    #prep forms to flash return to index for now

    print('test comment')
    return render_template('rendertest4.html', title='Render Test', archList=archList)

@app.route('/archSelect', methods=['POST'])
def archSelect():
    ss_client = ss_get_client(access_token)
     
    #addForm = archWeekForm()

    if request.method=='POST': #if one of the forms is submitted
        #print('request = '+ str(request))
        #print('request.form = '+ str(request.form))
        #print('request.data = '+ request.data)
        print('Arch Select function')
        print('request.data = '+ str(request.data))
        print('request.data decoded = '+ request.data.decode())
        
        
        dataString = request.data.decode()
        data = json.loads(dataString)
        #for i in data['arch']:
        #    print("{}    {}".format(i['name'],i['value']))   
        archSelect = data['arch'][0]['value']
        print(archSelect)
        if data['function'] == 'arch':
            #return jsonify({"status":"Updated successfully"})
            archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect=archSelect)
            return render_template('rendertest4.html', title='Render Test', archList=archList)
        else:
            return jsonify({"status":"Error"})
                    
    return render_template('rendertest3.html', title='Render Test', EN_list=EN_list)



@app.route('/remove', methods=['POST'])
def remove():
    ss_client = ss_get_client(access_token)
    archlist = ss_get_sheet_parsed(ss_client,archSheet, archSelect='EN') 
    #addForm = archWeekForm()

    if request.method=='POST': #if one of the forms is submitted
        #print('request = '+ str(request))
        #print('request.form = '+ str(request.form))
        #print('request.data = '+ request.data)
        #print('request.data decoded = '+ request.data.decode())
        dataString = request.data.decode()
        data = json.loads(dataString)
        for i in data:
            print(i)
        for i in data['removeRows']:
            print(i)        
        if data['function'] == 'remove':

            return jsonify({"status":"Updated successfully"})
    
                    
    return render_template('rendertest3.html', title='Render Test', EN_list=EN_list)

@app.route('/add', methods=['POST'])
def add():
    ss_client = ss_get_client(access_token)
    archlist = ss_get_sheet_parsed(ss_client,archSheet, archSelect='EN') 
    #addForm = archWeekForm()

    if request.method=='POST': #if one of the forms is submitted
        #print('request = '+ str(request))
        #print('request.form = '+ str(request.form))
        #print('request.data = '+ request.data)
        #print('request.data = '+ str(request.data))
        #print('request.data decoded = '+ request.data.decode())
        
        dataString = request.data.decode()
        data = json.loads(dataString)
        for i in data['addRow']:
            print("{}    {}".format(i['name'],i['value']))       
        if data['function'] == 'add':
            return jsonify({"status":"Updated successfully"})
        
                    
    return render_template('rendertest3.html', title='Render Test', EN_list=EN_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.debug = True
