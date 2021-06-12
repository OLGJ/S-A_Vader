### This file appends collected data to an existing excel document. One function for each flair.

#Imports
import requests
import time
import pandas as pd
from openpyxl import load_workbook

startTime = time.time()

#Scripts for each flair.
from discussion_comments import discussion_processing
from dd_comments import dd_processing
from yolo_comments import yolo_processing
from earningsthread_comments import earningsthread_processing
from news_comments import news_processing
from gain_comments import gain_processing
from loss_comments import loss_processing

#Load workbook.
workbook_name = 'wsb_data_week4.xlsx'
wb = load_workbook(workbook_name)


# Sheet titles:
# DD, Discussion, YOLO, News, Earningsthread, Gain, Loss
# Sheet headers:
# Date, ID, Comment, Parent_ID

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
    print('-----Begins Discussion process.-----')
    #Load data
    discussion_data = discussion_processing()
    df = pd.ExcelFile(workbook_name)
    
    #Selectors for correct sheet and date.
    active_sheeet=discussion_data[0][1]
    date=discussion_data[0][0]

    adds = 0

    #Split ID's into list with pandas.
    target_sheet = df.parse(active_sheeet)
    split_ids = target_sheet['ID'].unique()

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in discussion_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        if info[1] in split_ids:
            continue
        else:
            wb[active_sheeet].append(info)
            adds += 1

    #Save changes.
    df.close()
    wb.save(filename=workbook_name)
    print(f'New comments added successfully to wsb_data.\nFlair: {active_sheeet}\nAdded comments: {adds}')

def wsb_dd_appender():
    """
        This function loads the functions that collects DD data and stores data in an excel sheet.

        Loaded data structure:
        [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]+...+]

        Returned data structure (Excel):
        Date, ID, Submission, "Line=Submission"
        Date, ID, Comment, Parent id
        +
        ...
        +
    """
    print('-----Begins DD process.-----')
    #Load data
    dd_data = dd_processing()
    df = pd.ExcelFile(workbook_name)
    
    #Selectors for correct sheet and date.
    active_sheeet=dd_data[0][1]
    date=dd_data[0][0]

    adds = 0

    #Split ID's into list with pandas.
    target_sheet = df.parse(active_sheeet)
    split_ids = target_sheet['ID'].unique()

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in dd_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        if info[1] in split_ids:
            continue
        else:
            wb[active_sheeet].append(info)
            adds += 1

    #Save changes.
    df.close()
    wb.save(filename=workbook_name)
    print(f'New comments added successfully to wsb_data.\nFlair: {active_sheeet}\nAdded comments: {adds}')

def wsb_yolo_appender():
    """
        This function loads the functions that collects YOLO data and stores data in an excel sheet.

        Loaded data structure:
        [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]+...+]

        Returned data structure (Excel):
        Date, ID, Submission, "Line=Submission"
        Date, ID, Comment, Parent id
        +
        ...
        +
    """
    print('-----Begins YOLO process.-----')
    #Load data
    yolo_data = yolo_processing()
    df = pd.ExcelFile(workbook_name)
    
    #Selectors for correct sheet and date.
    active_sheeet=yolo_data[0][1]
    date=yolo_data[0][0]

    adds = 0

    #Split ID's into list with pandas.
    target_sheet = df.parse(active_sheeet)
    split_ids = target_sheet['ID'].unique()

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in yolo_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        if info[1] in split_ids:
            continue
        else:
            wb[active_sheeet].append(info)
            adds += 1

    #Save changes.
    df.close()
    wb.save(filename=workbook_name)
    print(f'New comments added successfully to wsb_data.\nFlair: {active_sheeet}\nAdded comments: {adds}')

def wsb_earningsthread_appender():
    """
        This function loads the functions that collects Earningsthread data and stores data in an excel sheet.

        Loaded data structure:
        [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]+...+]

        Returned data structure (Excel):
        Date, ID, Submission, "Line=Submission"
        Date, ID, Comment, Parent id
        +
        ...
        +
    """
    print('-----Begins earningsthread process.-----')
    #Load data
    earningsthread_data = earningsthread_processing()
    df = pd.ExcelFile(workbook_name)
    
    #Selectors for correct sheet and date.
    active_sheeet=earningsthread_data[0][1]
    date=earningsthread_data[0][0]

    adds = 0

    #Split ID's into list with pandas.
    target_sheet = df.parse(active_sheeet)
    split_ids = target_sheet['ID'].unique()

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in earningsthread_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        if info[1] in split_ids:
            continue
        else:
            wb[active_sheeet].append(info)
            adds += 1

    #Save changes.
    df.close()
    wb.save(filename=workbook_name)
    print(f'New comments added successfully to wsb_data.\nFlair: {active_sheeet}\nAdded comments: {adds}')

def wsb_news_appender():
    """
        This function loads the functions that collects News data and stores data in an excel sheet.

        Loaded data structure:
        [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]+...+]

        Returned data structure (Excel):
        Date, ID, Submission, "Line=Submission"
        Date, ID, Comment, Parent id
        +
        ...
        +
    """
    print('-----Begins News process.-----')
    #Load data
    news_data = news_processing()
    df = pd.ExcelFile(workbook_name)
    
    #Selectors for correct sheet and date.
    active_sheeet=news_data[0][1]
    date=news_data[0][0]

    adds = 0

    #Split ID's into list with pandas.
    target_sheet = df.parse(active_sheeet)
    split_ids = target_sheet['ID'].unique()

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in news_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        if info[1] in split_ids:
            continue
        else:
            wb[active_sheeet].append(info)
            adds += 1

    #Save changes.
    df.close()
    wb.save(filename=workbook_name)
    print(f'New comments added successfully to wsb_data.\nFlair: {active_sheeet}\nAdded comments: {adds}')

def wsb_gain_appender():
    """
        This function loads the functions that collects Gain data and stores data in an excel sheet.

        Loaded data structure:
        [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]+...+]

        Returned data structure (Excel):
        Date, ID, Submission, "Line=Submission"
        Date, ID, Comment, Parent id
        +
        ...
        +
    """
    print('-----Begins Gain process.-----')
    #Load data
    gain_data = gain_processing()
    df = pd.ExcelFile(workbook_name)
    
    #Selectors for correct sheet and date.
    active_sheeet=gain_data[0][1]
    date=gain_data[0][0]

    adds = 0

    #Split ID's into list with pandas.
    target_sheet = df.parse(active_sheeet)
    split_ids = target_sheet['ID'].unique()

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in gain_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        if info[1] in split_ids:
            continue
        else:
            wb[active_sheeet].append(info)
            adds += 1

    #Save changes.
    df.close()
    wb.save(filename=workbook_name)
    print(f'New comments added successfully to wsb_data.\nFlair: {active_sheeet}\nAdded comments: {adds}')

def wsb_loss_appender():
    """
        This function loads the functions that collects Loss data and stores data in an excel sheet.

        Loaded data structure:
        [[date, flair, ---], [submission id, submission, "Line=Submission"], [comment id, comment, comment parent_id]+...+]

        Returned data structure (Excel):
        Date, ID, Submission, "Line=Submission"
        Date, ID, Comment, Parent id
        +
        ...
        +
    """
    print('-----Begins Loss process.-----')
    #Load data
    loss_data = loss_processing()
    df = pd.ExcelFile(workbook_name)
    
    #Selectors for correct sheet and date.
    active_sheeet=loss_data[0][1]
    date=loss_data[0][0]

    adds = 0

    #Split ID's into list with pandas.
    target_sheet = df.parse(active_sheeet)
    split_ids = target_sheet['ID'].unique()

    #Loop datalist and add data to excel-sheet under the correct flair.
    for info in loss_data[1:]:
        #Insert date at index 0.
        info.insert(0, date)
        
        #Append data to wb.
        if info[1] in split_ids:
            continue
        else:
            wb[active_sheeet].append(info)
            adds += 1

    #Save changes.
    df.close()
    wb.save(filename=workbook_name)
    print(f'New comments added successfully to wsb_data.\nFlair: {active_sheeet}\nAdded comments: {adds}')


#Run functions
if __name__ == "__main__":
    wsb_discussion_appender()
    wsb_dd_appender()
    wsb_yolo_appender()
    wsb_earningsthread_appender()
    wsb_news_appender()
    wsb_gain_appender()
    wsb_loss_appender()

print ('The script took {0} second !'.format(time.time() - startTime))