
# Retrieve data from online API's

# Import requests

import requests

Data = requests.get("https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol=AAPL&apikey=xxxx8")

AAPL = Data.json()


# Import a CSV file into a Pandas Dataframe
# Import Pandas

import pandas as pd

SP_500_stockprices = pd.read_csv("SP 500 Stock Prices 2014-2017.csv")
print(type(SP_500_stockprices))

# Describe the type of file
print (SP_500_stockprices.info)

# sort the SP 500 stock prices by date

SP_500_stockprices_symbol = SP_500_stockprices.sort_values('symbol')

# Print the first and last few rows of the sorted dataframe.

print(SP_500_stockprices_symbol.head())
print(SP_500_stockprices_symbol.tail())

# Filter the SP 500 where the opening value is over 100
SP_500_open_100 = SP_500_stockprices_symbol[SP_500_stockprices_symbol['open']>100]

# Import CSV file into pandas for further analysis

Bestsellers = pd.read_csv('bestsellers with categories.csv')

# Print the file info for Bestsellers
print(Bestsellers.info())

# Using indexing print the first four rows from Bestsellers
print(Bestsellers[0:4])

# Extract the columns of authors and names from the data

Bestsellers_Author = Bestsellers.iloc[:,0:2]
print(Bestsellers_Author)

# Drop any duplication of titles of books
Bestsellers_Title = Bestsellers.drop_duplicates('Name').sort_values('Price', ascending=True)
print(Bestsellers_Title.head(12))

# Group the genre of books by fiction and non fiction and the average price

Bestsellers_Genre_avg_price = Bestsellers.groupby('Genre')['Price'].mean()
print(Bestsellers_Genre_avg_price)

# Group the Bestsellers by Genre and find the min, max, and average of fiction and non fiction for both prices and reviews

Bestsellers_stats = Bestsellers.groupby('Year')[['Price','Reviews']].agg([min,max,])
print(Bestsellers_stats)




