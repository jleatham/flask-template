from flask import Flask, render_template, flash, redirect, url_for, request, jsonify
from config import Config
from forms import LoginForm, archWeekForm, removeArchWeekForm
from test import testFunction
from myMarshmallow import Architecture, ArchitectureSchema
from mySmartSheet import access_token, archSheet, ss_get_client, ss_get_sheet_parsed, ss_update_row, ss_remove_rows, ss_get_events_parsed
from myEmail import create_html_msg
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
            print(archList)
            return render_template('rendertest4.html', title='Render Test', archList=archList)
        else:
            return jsonify({"status":"Error"})
                    
    return jsonify({"status":"Error"})

@app.route('/EN', methods=['GET'])
def EN():

    ss_client = ss_get_client(access_token)
    archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect='EN')
    return render_template('archTemplate.html', title='EN', metaID='EN', archList=archList)

@app.route('/SEC', methods=['GET'])
def SEC():

    ss_client = ss_get_client(access_token)
    archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect='SEC')
    return render_template('archTemplate.html', title='SEC', metaID='SEC', archList=archList)

@app.route('/DC', methods=['GET'])
def DC():

    ss_client = ss_get_client(access_token)
    archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect='DC')
    return render_template('archTemplate.html', title='DC', metaID='DC', archList=archList)

@app.route('/COLLAB', methods=['GET'])
def COLLAB():

    ss_client = ss_get_client(access_token)
    archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect='COLLAB')
    return render_template('archTemplate.html', title='COLLAB', metaID='COLLAB', archList=archList)

@app.route('/APP', methods=['GET'])
def APP():

    ss_client = ss_get_client(access_token)
    archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect='APP')
    return render_template('archTemplate.html', title='APP', metaID='APP', archList=archList)



@app.route('/remove', methods=['POST'])
def remove():
    ss_client = ss_get_client(access_token)

    if request.method=='POST': #if one of the forms is submitted

        dataString = request.data.decode()
        data = json.loads(dataString)
        removeRows = []

        for i in data['removeRows']:
            #print(i)  
            removeRows.append(i)      
        if data['function'] == 'remove':
            ss_remove_rows(ss_client,archSheet,removeRows)
            return jsonify({"status":"Updated successfully"})
    
                    
    #return render_template('rendertest3.html', title='Render Test', EN_list=EN_list)

@app.route('/add', methods=['POST'])
def add():
    ss_client = ss_get_client(access_token)


    if request.method=='POST': #if one of the forms is submitted

        dataString = request.data.decode()
        data = json.loads(dataString)
        print(data)
        for i in data['addRow']:
            print("{}    {}".format(i['name'],i['value']))    

        
            if i['name'] == 'category':
                category = i['value']                        
            if i['name'] == 'bullet':
                bullet = i['value']
            if i['name'] == 'bLink':
                bLink = i['value']
            if i['name'] == 'subBullet1':
                subBullet1 = i['value']
            if i['name'] == 'sb1Link':
                sb1Link = i['value']
            if i['name'] == 'subBullet2':
                subBullet2 = i['value']
            if i['name'] == 'sb2Link':
                sb2Link = i['value']
            if i['name'] == 'subBullet3':
                subBullet3 = i['value']
            if i['name'] == 'sb3Link':
                sb3Link = i['value']
            if i['name'] == 'subBullet4':
                subBullet4 = i['value']
            if i['name'] == 'sb4Link':
                sb4Link = i['value']
            if i['name'] == 'subBullet5':
                subBullet5 = i['value']
            if i['name'] == 'sb5Link':
                sb5Link = i['value']
        arch = data['arch']['name']
        
        if data['function'] == 'add':

            now  = datetime.now()
            date = now.strftime("%d %b %Y")  
            print('made it to addForm validate')
            archObject = Architecture(date, arch, category, bullet, bLink,
                subBullet1, sb1Link, subBullet2, sb2Link,
                subBullet3, sb3Link, subBullet4, sb4Link,
                subBullet5, sb5Link, 12345678) #random row ID since we just post to bottom
            schema = ArchitectureSchema()
            archDict, errors = schema.dump(archObject) 
            rowAddResult = ss_update_row(ss_client,archSheet, archDict)    


            return jsonify({"status":"Updated successfully"})
        
                    
    #return render_template('rendertest3.html', title='Render Test', EN_list=EN_list)

@app.route('/emailTest', methods=['GET'])
def emailTest():
    #add an 'all' for archSelect and return ENList, SECList, etc all at once
    ss_client = ss_get_client(access_token)
    archList = ss_get_sheet_parsed(ss_client,archSheet,archSelect='EN')    
    emailData = create_html_msg(archList)

    return render_template('emailTest.html', title='email', metaID='email', emailData=emailData)

@app.route('/eventTemplate', methods=['GET'])
def events():
    ss_client = ss_get_client(access_token)
    eventList = ss_get_events_parsed(ss_client,eventSheet,eventSelect='ALL')
    return render_template('eventTemplate.html', title='events', metaID='events', eventList=eventList)

@app.route('/eventRemove', methods=['POST'])
def eventRemove():
    print('eventRemove Route')
    return render_template('eventTemplate.html', title='events', metaID='events')

@app.route('/eventAdd', methods=['POST'])
def eventAdd():
    print('eventAdd Route')
    
    if request.method=='POST': #if one of the forms is submitted

        dataString = request.data.decode()
        data = json.loads(dataString)
        print(data)
        for i in data['addRow']:
            print("{}    {}".format(i['name'],i['value']))       
    return render_template('eventTemplate.html', title='events', metaID='events')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    app.debug = True
