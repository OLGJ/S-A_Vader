#stocks

#Imports
import csv
import os

"""Filters all stocks with a pricing above or equal to 5$ from csv file retrieved 2021-03-29"""
def stocks():
    with open(r'C:\Users\Olof\Skola\Kurser\729G40\nasdaq_screener_1617017873723.csv', 'r') as csv_stocks:

        #Symbol,Name,Last Sale,Net Change,% Change,Market Cap,Country,IPO Year,Volume,Sector,Industry
        csvreader = csv.reader(csv_stocks, delimiter = ',')
        next(csvreader)

        stock_list = []

        #Loops through file and filters stocks that are above 5$
        for row in csvreader:
            stock_price = float(row[2].replace("$", ""))
            if stock_price >= 5:
                stock_list.append(row[0])


        csv_stocks.close()
        

if __name__ == "__main__":
	stocks()
