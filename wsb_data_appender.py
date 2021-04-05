### This file appends collected data to an existing excel document. One function for each flair to simplify callings with redis.

#Imports
import requests
from openpyxl import load_workbook
from discussion_comments import discussion_processing
#TODO other functions.


#Parameters: Sheet titles and headers in sheets.
titles = ["DD", "Discussion", "YOLO", "News", "Earningsthread"]
headers = ["Date", "ID", "Comment"]
#date = datetime.datetime.now().strftime("%x")

#Load workbook
workbook_name = 'wsb_data.xlsx'
wb = load_workbook(workbook_name)

def wsb_discussion_appender():
    """
        This function loads the functions that collects discussion data and stores data in an excel sheet.

        Loaded data structure:
        [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]+...+]

        Returned data structure (Excel):
        Date, ID, Submission, "Line=Submission"
        Date, ID, Comment, Parent id
        +
        ...
        +
    """
    
    #Load data
    discussion_data = discussion_processing()
    
    #Selectors for correct sheet and date.
    active_sheeet=discussion_data[0][1]
    date=discussion_data[0][0]

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in discussion_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        wb[active_sheeet].append(info)

    #Save changes.
    wb.save(filename=workbook_name)



def run_data_adder():
    """
        Function to run rq.
    """
    print('kommer hit')
    resp = wsb_discussion_appender()
    return resp

#Run functions
if __name__ == "__main__":
    wsb_discussion_appender()
    run_data_adder()
    