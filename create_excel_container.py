### This file creates an excel document for the collected data.

#Imports
from openpyxl import Workbook

#Create workbook
workbook_name = 'wsb_data.xlsx'

titles = ["DD", "Discussion", "YOLO", "News", "Earningsthread"]
headers = ["Date", "ID", "Comment"]
wb = Workbook()

#Creates a sheet title for each flair and gives it headers.
for title in titles:
    wb.create_sheet(title)
    page = wb[title]
    page.append(headers)

#Remove default sheet and save file.
del wb['Sheet']
wb.save(filename=workbook_name)


