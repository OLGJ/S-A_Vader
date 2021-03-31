### This file appends collected data to an existing excel document.

#Imports
from openpyxl import load_workbook
import datetime
#load data
import discussion_comments


#Parameters
titles = ["DD", "Discussion", "YOLO", "News", "Earningsthread"]
headers = ["Date", "ID", "Comment"]
#date = datetime.datetime.now().strftime("%x")

#Load workbook
workbook_name = 'wsb_data.xlsx'
wb = load_workbook(workbook_name)

def wsb_appender():
    """
        This function loads the functions that collects data and stores them in the excel sheet.

        Loaded data structure:
        [[date, flair], [id, comment]]
    """
    discussion_data = discussion_comments.discussion_data()
    active_sheeet=discussion_data[0][1]
    date=discussion_data[0][0]
    #print('act', active_sheeet)
    #print('date', date)

    for info in discussion_data[1:]:
        info.insert(0, date)
        wb[active_sheeet].append(info)

    wb.save(filename=workbook_name)



#Run functions
if __name__ == "__main__":
    wsb_appender()
    