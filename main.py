
# Retrieve data from online API's

# Import requests

import requests

Data = requests.get("https://www.alphavantage.co/query?function=EARNINGS&symbol=AAPL&apikey=xxxxxxxxxx")

AAPL = Data.json()

print(AAPL)

# Import a CSV file into a Pandas Dataframe
# Import Pandas

import pandas as pd

SP_500_stockprices = pd.read_csv("SP 500 Stock Prices 2014-2017.csv")
print(type(SP_500_stockprices))

# Describe the type of file
print (SP_500_stockprices.info())

# sort the SP 500 stock prices by symbol in descending order

SP_500_stockprices_symbol = SP_500_stockprices.sort_values('symbol',ascending = False)

# Print the first and last few rows of the sorted dataframe.

print(SP_500_stockprices_symbol.head())
print(SP_500_stockprices_symbol.tail())

# Filter the SP 500 where the opening value is over 100
SP_500_open_100 = SP_500_stockprices_symbol[SP_500_stockprices_symbol['open']>100]
print(SP_500_open_100.head(12))

# Import CSV file into pandas for further analysis

Bestsellers = pd.read_csv('bestsellers with categories.csv')

# Print the file info for Bestsellers
print(Bestsellers.info())

# Using indexing print the first four rows from Bestsellers
print(Bestsellers[0:4])

# Extract the columns of authors and names from the data

Bestsellers_Author = Bestsellers.iloc[:,0:2]
print(Bestsellers_Author.head(10))

# Drop any duplication of titles of books
Bestsellers_Title = Bestsellers.drop_duplicates('Name').sort_values('Price', ascending=True)
print(Bestsellers_Title.head(12))

# Group the genre of books by fiction and non fiction and the average price

Bestsellers_Genre_avg_price = Bestsellers.groupby('Genre')['Price'].mean()
print(Bestsellers_Genre_avg_price)

# Group the Bestsellers by year and find the min, max, and average of fiction and non fiction for both prices and reviews

Bestsellers_stats = Bestsellers.groupby('Year')[['Price','Reviews']].agg([min,max,])
print(Bestsellers_stats)

# Import two cvs files into panda dataframes

FB = pd.read_csv('FB_data.csv')
AMZN = pd.read_csv('AMZN_data.csv')

# Review the info and first few roads of this dataframes
print(FB.info())
print(AMZN.info())

import datetime as datetime

# Convert the date column to datetime
FB.date = pd.to_datetime(FB.date)
FB.set_index('date', inplace = True)

# Review the info and first few roads of this dataframes
print(FB.info())

AMZN.date = pd.to_datetime(AMZN.date)
AMZN.set_index('date', inplace = True)

print(AMZN.info)
print(AMZN.head())

#Show the data from Dec 2015 to Dec 2016
print(FB.loc["2015-12":"2016-12"])

#Merge the two datasets using pd.merge ordered and merge by date.

FB_AMZN_Data = pd.merge(FB,AMZN, how='inner', left_index=True, right_index=True,suffixes = ('_fb','_amzn'))
print(FB_AMZN_Data)

# Get the median of the opening prices
FB_open = FB.loc[:,'open'].median()
print(FB_open)

# Get the median of the closing prices
FB_close = FB.loc[:,'close'].median()
print(FB_close)

# Show if the opening and closing stock is trending down
if FB_open < FB_close:
    print("Trending down.")

# Merge the two datasets using pd.merge ordered and merge by date.

FB_AMZN_Data = pd.merge(FB, AMZN, how='inner', left_index=True, right_index=True, suffixes=('_fb', '_amzn'))
print(FB_AMZN_Data)

# Import numpy as the alias np
import numpy as np

# set up an array for open prices and calculate the mean of the open prices
FB_open= np.array(FB['open'])
print(FB_open)
open_mean = np.mean(FB_open)
print(open_mean)

AMZN_open=np.array(AMZN['open'])

# Using boolean array select only where the open prices are over 180
boolean_array = FB_open > 180
print(FB_open[boolean_array])

# Import matplotlib

import matplotlib.pyplot as plt

# Set up a plot of the closing stock prices for FB showing both closing and opening stocks

# Initalise a Figure and Axes
fig, ax = plt.subplots()
ax.set_title('Facebook closing stock')

# Add the time-series for "close" to the plot
ax.plot(FB.index,FB['close'])

# Set the x-axis label to YEAR
ax.set_xlabel('Year')

# Set the Y label to CLOSE
ax.set_ylabel('CLOSE')

fig.set_size_inches([7, 9])
fig.savefig('figure_1_1.png')

# Initalize a Figure and Axes
fig, ax = plt.subplots()
ax.set_title('Facebook closing and volume')
# Plot the close variable in blue
ax.plot(FB.index, FB["close"], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the volume in red
ax2.plot(FB.index, FB["volume"], color='red')

fig.set_size_inches([7, 9])
fig.savefig('figure_1_2.png')

# Initalise a Figure and Axes
fig, ax = plt.subplots()
ax.set_title('Amazon closing stock')

# Add the time-series for "close" to the plot
ax.plot(AMZN.index,AMZN['close'])

# Set the x-axis label to YEAR
ax.set_xlabel('Year')

# Set the Y label to CLOSE
ax.set_ylabel('CLOSE')

fig.set_size_inches(5, 7)
fig.savefig('figure_1_3.png')

# Initalize a Figure and Axes
fig, ax = plt.subplots()
ax.set_title('Amazon close and volume')
# Plot the close variable in blue
ax.plot(AMZN.index, AMZN["close"], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the volume in red
ax2.plot(AMZN.index, AMZN["volume"], color='red')

fig.set_size_inches([7, 9])
fig.savefig('figure_1_4.png')





