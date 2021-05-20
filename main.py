
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


