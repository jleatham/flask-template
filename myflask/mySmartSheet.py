import smartsheet
import os

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

def ss_get_sheet_parsed(ss_client,sheet):
    pass
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

