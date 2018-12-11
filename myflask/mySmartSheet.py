import smartsheet
import os
#from datetime import datetime
from myMarshmallow import Architecture, ArchitectureSchema, Event, EventSchema
import json
from secrets import SMARTSHEET_TOKEN
import requests

#can't seem to get wsgi to accept environment var
#access_token = os.environ.get('SMARTSHEET_TOKEN')
access_token = SMARTSHEET_TOKEN
archSheet = 2089577960761220
eventSheet = 2175182816208772

#testing, delete
#from mySmartSheet import access_token, archSheet, ss_get_client, ss_get_sheet_parsed, ss_update_row
#ss_client = ss_get_client(access_token)
#EN_list = ss_get_sheet_parsed(ss_client, archSheet)
#for i in EN_list:
#   print(i.bullet)

# Initialize client
def ss_get_client(access_token):
    ss_client = smartsheet.Smartsheet(access_token)
    # Make sure we don't miss any errors
    ss_client.errors_as_exceptions(True)
    return ss_client

#ss_client.assume_user("jleatham@cisco.com") #Doesn't work, don't need


def ss_get_all_sheets(ss_client):
    #List Org Sheets
    #response = ss_client.Sheets.list_org_sheets()  #dont have ord admin access
    response = ss_client.Sheets.list_sheets(include_all=True)
    return response.data

def ss_get_sheet_raw(ss_client,sheet):
    #Get Sheet
    return ss_client.Sheets.get_sheet(sheet) 


def ss_get_sheet_parsed(ss_client,sheet, archSelect='EN'):
    #Want to be able to get all archWeek info and seperate from json into dict
    #should I do this as a sheet all at once or function for seperate row
    #and then do multiple API calls 1 per row.  That would be ineffective I think
    #need to be able to find specific row based on ID and delete
    #need to be able to loop through all rows, seperate based on architecture
    #then print out formatted based on type
    #Maybe I could make each arch type a class, i.e., EN, SEC, DC, etc
    #then each class would look like 
    # archClassName(object):
    #   def __init__ etc
    #       self.type   #intro, social, capital
    #       self.rowID
    #       self.timestamp
    #       self.mainBullet
    #       self.mainBulletLink
    #       self.subBullet1
    #       etc
    #       def convert_file_to_box_link(self.?) #How would this work?
    #use marshmallow schema, I think, still not sure how this makes life better
    #  marshmallow is used because a python class cannot easily be converted
    #  to simple types like dict or strings.  Marshmallow schema does that
    #Then when I loop through a row of API data, I can detect what arch it is
    # then assign it as a new archClass Object.  That object I can place in a
    # [] list, so that when it comes time to print the data, I can send all
    #arch specific data(like EN) all at once in the single list.
    #I could then loop through it
    # for i in list:
        #if i.type == 'intro':
            #print(i.mainBullet)
    

    jsonSheet = json.loads(str(ss_client.Sheets.get_sheet(sheet)))

    EN_list     = []
    SEC_list    = []
    DC_list     = []
    COLLAB_list = []
    APP_list    = []



    for x in jsonSheet['rows']:
        #print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))
        #reset all vars to empty for each row loop
        date        = ""
        arch        = ""
        #internal    = ""
        category    = ""
        bullet      = ""
        bLink       = ""
        subBullet1  = ""
        sb1Link     = ""
        subBullet2  = ""
        sb2Link     = ""
        subBullet3  = ""
        sb3Link     = ""
        subBullet4  = ""
        sb4Link     = ""
        subBullet5  = ""
        sb5Link     = ""
        rowID = x['id']
        for i in x['cells']:
            if 'value' in i:
                #print("\tcell id:{}    value: {}".format(i['columnId'],i['value']))
                if i['columnId'] == 6004582892496772:
                    date = i['value']            
                #if i['columnId'] == 8256382706182020:
                #    internal = i['value']
                if i['columnId'] == 938033311704964:
                    category = i['value']                        
                if i['columnId'] == 5441632939075460:
                    bullet = i['value']
                if i['columnId'] == 3189833125390212:
                    bLink = i['value']
                if i['columnId'] == 425317295777668:
                    subBullet1 = i['value']
                if i['columnId'] == 8588091620386692:
                    sb1Link = i['value']
                if i['columnId'] == 4084491993016196:
                    subBullet2 = i['value']
                if i['columnId'] == 6336291806701444:
                    sb2Link = i['value']
                if i['columnId'] == 1832692179330948:
                    subBullet3 = i['value']
                if i['columnId'] == 7462191713544068:
                    sb3Link = i['value']
                if i['columnId'] == 2958592086173572:
                    subBullet4 = i['value']
                if i['columnId'] == 5210391899858820:
                    sb4Link = i['value']
                if i['columnId'] == 706792272488324:
                    subBullet5 = i['value']
                if i['columnId'] == 8025141666965380:
                    sb5Link = i['value']
                if i['columnId'] == 3752783078811524:   #arch
                    arch = i['value']
        #after each cell is saved in whole row, create a data object
        #probably should just build the dict out manually as opposed to marshmall object first
        archObject = Architecture(date,arch,category,bullet,bLink,subBullet1,sb1Link,subBullet2,sb2Link,subBullet3,sb3Link,subBullet4,sb4Link,subBullet5,sb5Link, rowID)
        schema = ArchitectureSchema()
        archDict, errors = schema.dump(archObject)
        if arch == 'EN':
            EN_list.append(archDict)    
        elif arch == 'SEC':
            SEC_list.append(archDict)  
        elif arch == 'DC':
            DC_list.append(archDict)  
        elif arch == 'COLLAB':
            COLLAB_list.append(archDict)  
        elif arch == 'APP':
            APP_list.append(archDict)  

    if archSelect == 'EN':
        return EN_list
    elif archSelect == 'SEC':
        return SEC_list
    elif archSelect == 'DC':
        return DC_list
    elif archSelect == 'COLLAB':
        return COLLAB_list
    elif archSelect == 'APP':
        return APP_list
    elif archSelect == 'ALL':
        return EN_list, SEC_list, DC_list, COLLAB_list, APP_list


def ss_update_row(ss_client,sheetSelect,rowData):
    #would the above classes help me write a row of data based on form entry?
    #in the form, i would get all the specifc data for the row, I don't think
    #I would need it as a class, because I am just going to punt it to sheets
    # that is done by row, with the individual cell data like this:
    # ss_update_row(ss_client, arch='', type='',internal='',mainBullet='',etc):
    #   new_row=...
    #   new_row.id = get_first_available_row()
    #
    #   new_cell= ...
    #   new_cell.value= arch
    #   new_cell.column_id = manually typed column_id
    #   etc
    #
    #   rew_row.append(new_cell)
    #
    #   new_cell= ...
    #   new_cell.value= type
    #   new_cell.column_id = manually typed column_id
    #   etc
    #
    #   rew_row.append(new_cell)
    # 
    #   etc
    #   etc
    #
    #   update_row_function([new_row])


    #trying with requests instead of SDK
    headers = {'Authorization': "Bearer "+access_token,'Content-Type': "application/json"}
    url = "https://api.smartsheet.com/2.0/sheets/"+str(sheetSelect)+"/rows"
    if sheetSelect == archSheet:
        payload = '{"toBottom":true, "cells": [ \
                    {"columnId": 6004582892496772, "value": "'+ rowData["date"] +'",       "strict": false}, \
                    {"columnId": 938033311704964,  "value": "'+ rowData["category"] +'",   "strict": false}, \
                    {"columnId": 5441632939075460, "value": "'+ rowData["bullet"] +'",     "strict": false}, \
                    {"columnId": 3189833125390212, "value": "'+ rowData["bLink"] +'",      "strict": false}, \
                    {"columnId": 425317295777668,  "value": "'+ rowData["subBullet1"] +'", "strict": false}, \
                    {"columnId": 8588091620386692, "value": "'+ rowData["sb1Link"] +'",    "strict": false}, \
                    {"columnId": 4084491993016196, "value": "'+ rowData["subBullet2"] +'", "strict": false}, \
                    {"columnId": 6336291806701444, "value": "'+ rowData["sb2Link"] +'",    "strict": false}, \
                    {"columnId": 1832692179330948, "value": "'+ rowData["subBullet3"] +'", "strict": false}, \
                    {"columnId": 7462191713544068, "value": "'+ rowData["sb3Link"] +'",    "strict": false}, \
                    {"columnId": 2958592086173572, "value": "'+ rowData["subBullet4"] +'", "strict": false}, \
                    {"columnId": 5210391899858820, "value": "'+ rowData["sb4Link"] +'",    "strict": false}, \
                    {"columnId": 706792272488324,  "value": "'+ rowData["subBullet5"] +'", "strict": false}, \
                    {"columnId": 8025141666965380, "value": "'+ rowData["sb5Link"] +'",    "strict": false}, \
                    {"columnId": 3752783078811524, "value": "'+ rowData["arch"] +'",       "strict": false} \
                    ] }'
    elif sheetSelect == eventSheet:
        payload = '{"toBottom":true, "cells": [ \
                    {"columnId": 433964541339524,  "value": "'+ rowData["date"] +'",    "strict": false}, \
                    {"columnId": 4937564168710020, "value": "'+ rowData["city"] +'",    "strict": false}, \
                    {"columnId": 2685764355024772, "value": "'+ rowData["address"] +'", "strict": false}, \
                    {"columnId": 1559864448182148, "value": "'+ rowData["summary"] +'", "strict": false}, \
                    {"columnId": 6095620495697796, "value": "'+ rowData["content"] +'", "strict": false}, \
                    {"columnId": 3843820682012548, "value": "'+ rowData["reg"] +'",     "strict": false}, \
                    {"columnId": 8347420309383044, "value": "'+ rowData["email"] +'",   "strict": false}, \
                    {"columnId": 8596738865948548, "value": "'+ rowData["region"] +'",  "strict": false}, \
                    {"columnId": 7189363982395268, "value": "'+ rowData["arch"] +'",    "strict": false} \
                    ] }' 


    response = requests.request("POST", url, data=payload, headers=headers)
    responseJson = json.loads(response.text)
    return responseJson['message']


def ss_remove_rows(ss_client,sheetSelect,removeRows):
    ss_client.Sheets.delete_rows(
        sheetSelect,                       # sheet_id
        removeRows)     # row_ids



def ss_get_events_parsed(ss_client,eventSheet, eventSelect='ALL'):
    print('made it to events_parsed Function')
    jsonSheet = json.loads(str(ss_client.Sheets.get_sheet(eventSheet)))
    print('API returned')
    EN_list     = []
    SEC_list    = []
    DC_list     = []
    COLLAB_list = []
    APP_list    = []
    ALL_list    = []

    print(jsonSheet)
    print(jsonSheet['rows'])
    #need a fix for if event sheet is ever empty
    for x in jsonSheet['rows']:
        #print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))
        #reset all vars to empty for each row loop
        date        = ""
        arch        = ""
        region      = ""
        city        = ""
        address     = ""
        content     = ""
        summary     = ""
        reg         = ""
        email       = ""
        rowID       = x['id']
        for i in x['cells']:
            if 'value' in i:
                #print("\tcell id:{}    value: {}".format(i['columnId'],i['value']))
                if i['columnId'] == 433964541339524:
                    date = i['value']            
                #if i['columnId'] == 8256382706182020:
                #    internal = i['value']
                if i['columnId'] == 4937564168710020:
                    city = i['value']                        
                if i['columnId'] == 2685764355024772:
                    address = i['value']
                if i['columnId'] == 7189363982395268:
                    arch = i['value']
                if i['columnId'] == 1559864448182148:
                    summary = i['value']
                if i['columnId'] == 6095620495697796:
                    content = i['value']
                if i['columnId'] == 3843820682012548:
                    reg = i['value']
                if i['columnId'] == 8347420309383044:
                    email = i['value']
                if i['columnId'] == 8596738865948548:
                    region = i['value']
                print(i)
        #after each cell is saved in whole row, create a data object
        #probably should just build the dict out manually as opposed to marshmall object first
        
        eventObject = Event(date, arch, region, city, address, content, summary, reg, email, rowID)
        schema = EventSchema()
        eventDict, errors = schema.dump(eventObject)
        if arch == 'EN':
            EN_list.append(eventDict)    
        elif arch == 'SEC':
            SEC_list.append(eventDict)  
        elif arch == 'DC':
            DC_list.append(eventDict)  
        elif arch == 'COLLAB':
            COLLAB_list.append(eventDict)  
        elif arch == 'APP':
            APP_list.append(eventDict)


    if eventSelect == 'EN':
        return EN_list
    elif eventSelect == 'SEC':
        return SEC_list
    elif eventSelect == 'DC':
        return DC_list
    elif eventSelect == 'COLLAB':
        return COLLAB_list
    elif eventSelect == 'APP':
        return APP_list
    elif eventSelect == 'ALL':
        ALL_list = EN_list + SEC_list + DC_list + COLLAB_list + APP_list
        return ALL_list
