#! /usr/bin/env python

# Script for collecting volume data.

#Imports
import csv
import os

def volume():
    """
    Collects volume and price from csv file.
    """

    #List of tickers to look for.
    ticker_list = ['GME', 'PLTR','TSLA', 'AAPL', 'ASO', 'APHA', 'AMC', 'VIAC', 'MVIS', 'CLOV', 'AMD', 'BABA', 'NIO', 'BB']

    iter = 0
    #Nasdaq screener
    for i in ticker_list:
        stock_list = [['Stock', 'Date', 'Volume', 'Price']]        
        with open(r'C:\Users\Olof\Skola\Kurser\729G40\{i}.csv'.format(i=i), 'r') as csv_nasdaq:

            #Date,Open,High,Low,Close,Adj Close,Volume
            csvreader = csv.reader(csv_nasdaq, delimiter = ',')

            #Loops through file and filters info about stock
            #[stock, date, volume, price]
                        
            n = 0
            for row in csvreader:
                
                if n > 0:
                    stock_info = []
                    date, stock_volume, stock_price = row[0], row[6], row[4]
                    date = int(date[8:])-5                   
                    stock_info.append(i)
                    stock_info.append(date)
                    stock_info.append(int(stock_volume))
                    stock_info.append(float(stock_price))
                    stock_list.append(stock_info)
                n += 1

            csv_nasdaq.close()
        
        final_gme_stocks = []
        stocks_with_fancy_object_store = []

        object_model_keys = stock_list.pop(0)

        for stock in stock_list:
            stocks_with_fancy_object_store.append(
                {
                    object_model_keys[0]: stock[0],
                    object_model_keys[1]: stock[1],
                    object_model_keys[2]: stock[2],
                    object_model_keys[3]: stock[3],
                }
            )

        #Missing dates (weekend)
        missing_gme_dates = [5,6,12,13]

        for date in missing_gme_dates:
            upper_bound_found = False

            total_price = 0
            total_volume = 0

            for fancy_stock_object in stocks_with_fancy_object_store:
                if fancy_stock_object["Date"] == date - 1:
                    total_volume += float(fancy_stock_object["Volume"])
                    total_price += float(fancy_stock_object["Price"])

                if fancy_stock_object["Date"] == date + 1:
                    total_volume += float(fancy_stock_object["Volume"])
                    total_price += float(fancy_stock_object["Price"])
                    upper_bound_found = True

            if upper_bound_found == False :
                for fancy_stock_object in stocks_with_fancy_object_store:

                    if fancy_stock_object["Date"] == date + 2 and upper_bound_found == False:
                        print("Added to date + 2," + str(date))
                        total_volume += float(fancy_stock_object["Volume"])
                        total_price += float(fancy_stock_object["Price"])
                        upper_bound_found = True

            stocks_with_fancy_object_store.append(
                {
                    "Stock": stock_list[1][0],
                    "Date": date,
                    "Volume": str(total_volume / 2),
                    "Price": str(total_price / 2),
                }
            )

        final_gme_stocks = sorted(stocks_with_fancy_object_store, key=lambda k: k["Date"])

        keys = final_gme_stocks[0].keys()

        with open(r'C:\Users\Olof\Skola\Kurser\729G40\wallstreet_data.csv', 'a', newline='') as output_file:
            
            if iter < 1:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(final_gme_stocks)
            else:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writerows(final_gme_stocks)

            iter += 1
            output_file.close()

if __name__ == "__main__":
	volume()