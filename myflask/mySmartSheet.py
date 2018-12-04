import smartsheet
import os
#from datetime import datetime
from myMarshmallow import Architecture, ArchitectureSchema
import json

access_token = SECRET_KEY = os.environ.get('SMARTSHEET_TOKEN')
archSheet = 2089577960761220

# Initialize client
def ss_get_client():
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

'''
jsonSheet = json.loads(str(sheet))

column title: date    ID: 6004582892496772
column title: architecture    ID: 3752783078811524
column title: internal    ID: 8256382706182020
column title: category    ID: 938033311704964
column title: bullet    ID: 5441632939075460
column title: bLink    ID: 3189833125390212
column title: subBullet1    ID: 425317295777668
column title: sb1Link    ID: 8588091620386692
column title: subBullet2    ID: 4084491993016196
column title: sb2Link    ID: 6336291806701444
column title: subBullet3    ID: 1832692179330948
column title: sb3Link    ID: 7462191713544068
column title: subBullet4    ID: 2958592086173572
column title: sb4Link    ID: 5210391899858820
column title: subBullet5    ID: 706792272488324
column title: sb5Link    ID: 8025141666965380



for x in jsonSheet['rows']:
    print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))

id: 434515023816580    rowNumber: 1
id: 4938114651187076    rowNumber: 2
id: 2686314837501828    rowNumber: 3
id: 7189914464872324    rowNumber: 4
id: 1560414930659204    rowNumber: 5
id: 6064014558029700    rowNumber: 6
id: 3812214744344452    rowNumber: 7
id: 8315814371714948    rowNumber: 8
id: 997464977237892    rowNumber: 9
id: 5501064604608388    rowNumber: 10
id: 3249264790923140    rowNumber: 11
id: 7752864418293636    rowNumber: 12
id: 2123364884080516    rowNumber: 13
id: 6626964511451012    rowNumber: 14
id: 4375164697765764    rowNumber: 15
id: 8878764325136260    rowNumber: 16
id: 82671302928260    rowNumber: 17
id: 4586270930298756    rowNumber: 18




for x in jsonSheet['rows']:
     print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))
     for i in x['cells']:
             if 'value' in i:
                     print("\tcell id:{}    value: {}".format(i['columnId'],i['value']))



    #now  = datetime.now()
    #date = now.strftime("%d %b %Y")
EN_list     = []
SEC_list    = []
DC_list     = []
COLLAB_list = []
APP_list    = []



for x in jsonSheet['rows']:
    print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))
    #reset all vars to empty
    date        = ""
    internal    = ""
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
    ss_dict= {}  
    for i in x['cells']:
        if 'value' in i:
            print("\tcell id:{}    value: {}".format(i['columnId'],i['value']))
            if i['columnId'] == 6004582892496772:
                date = i['value']            
            if i['columnId'] == 8256382706182020:
                internal = i['value']
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
            ss_dict = {'date':date,'internal':internal,'category':category,'bullet':bullet,'bLink':bLink,'subBullet1':subBullet1,'sb1Link':sb1Link,'subBullet2':subBullet2,'sb2Link':sb2Link,'subBullet3':subBullet3,'sb3Link':sb3Link,'subBullet4':subBullet4,'sb4Link':sb4Link,'subBullet5':subBullet5,'sb5Link':sb5Link}         
            schema = ArchitectureSchema()
            archResult = schema.load(ss_dict)
            if i['columnId'] == 3752783078811524:   #arch
                if i['value'] == 'EN':
                    EN_list.append(archResult)

'''

def ss_get_sheet_parsed(ss_client,sheet):
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
        print("id: {}    rowNumber: {}".format(x['id'],x['rowNumber']))
        #reset all vars to empty
        date        = ""
        internal    = ""
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
        ss_dict= {}  
        for i in x['cells']:
            if 'value' in i:
                print("\tcell id:{}    value: {}".format(i['columnId'],i['value']))
                if i['columnId'] == 6004582892496772:
                    date = i['value']            
                if i['columnId'] == 8256382706182020:
                    internal = i['value']
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
                ss_dict = {'date':date,'internal':internal,'category':category,'bullet':bullet,'bLink':bLink,'subBullet1':subBullet1,'sb1Link':sb1Link,'subBullet2':subBullet2,'sb2Link':sb2Link,'subBullet3':subBullet3,'sb3Link':sb3Link,'subBullet4':subBullet4,'sb4Link':sb4Link,'subBullet5':subBullet5,'sb5Link':sb5Link}         
                schema = ArchitectureSchema()
                archResult = schema.load(ss_dict)
                if i['columnId'] == 3752783078811524:   #arch
                    if i['value'] == 'EN':
                        EN_list.append(archResult)    
                    ###Add the rest
    return EN_list



def ss_update_row():
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

    #Update Cells inside Row

    # Build new cell value
    new_cell = ss_client.models.Cell()
    new_cell.column_id = 7036894123976580
    new_cell.value = "new value"
    new_cell.strict = False

    # Build the row to update
    new_row = ss_client.models.Row()
    new_row.id = 6809535313667972
    new_row.cells.append(new_cell)

    # Update rows
    updated_row = ss_client.Sheets.update_rows(
    2068827774183300,      # sheet_id
    [new_row])

