# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IflY9yNy5L6oyVz6gmAqMadIGT95XpHP

# Data Preprartion and Cleaning
"""

import pandas as pd

df = pd.read_csv("/content/TSLA.csv")

df.head()

df.head(20)

df.tail()

## lets see the shape of dataframe to get the rows and columns in the dataframe

df.shape

df.info()

df.describe()

#check the null value
df.isnull().sum()

# list of column
df.columns

df[['Date', 'Close']]

df



"""# Exploratory Analysis and Visualization"""

# extract year, month, day from string format date

df['Date'] = pd.to_datetime(df.Date)
df['Year'] = pd.DatetimeIndex(df.Date).year
df['Month'] = pd.DatetimeIndex(df.Date).month
df['Day'] = pd.DatetimeIndex(df.Date).day

df



Total_transaction = df['Date'].count()
print("The total transaction in given ten year is {}".format(Total_transaction))

"""# Q.1 What is the mean closing prices in each year?"""

closing_mean = df.groupby('Year')[['Date', 'Open', 'Close', 'Volume']].mean()
closing_mean

import matplotlib.pyplot as plt

plt.title('TSLA Stock')
plt.xlabel('year')
plt.ylabel('close price in USD')
plt.plot(df['Year'], df['Close'])

import seaborn as sns



#  trend of the stock prices

sns.set_style("darkgrid")
plt.figure(figsize = (26, 18))
plt.title("trend of the stock prices")
plt.xlabel("Date")
plt.ylabel("Closed Price")
plt.plot(df['Date'], df['Close'])
plt.show()

# Sort high to low
high_to_low = df.sort_values('Volume', ascending = False)
high_to_low

high_to_low.head(1)

high_to_low.tail(1)



total_distribution = df.groupby('Year')[['Volume']].sum()
total_distribution

sns.barplot(total_distribution.index, total_distribution.Volume, data=df )

"""# The above bar graph shows that the traded stock in year 2019 is in the higher distribution. We can also find the variation in such barplot figure for know the difference between the actual value and the value just above the data shown in the bar top limit.

# Inferences and Conclusion
- The data analysis is much easier using the python pandas numerical applications , i have tried to use most common interesting analysis method or this project which helped me alot in understanding many basic knowledge of the analysis with python pandas. 
- I have concluded that stock of Tesla Incoporation has increased value of its per stock price with time. 
- I have also found that in the recent year the price of TESLA stock has increased very hugely.
- The stock analysis has other many application i have only covered basic here and i learned many other interesting facts like predictions of stock , stock optimization and i am still trying learn those ) 
- From this project i got to learn so much and there are much more to learn and i will be interested to learn more , I found myself so much focused and did helped me for collecting and refining data and use as per requirement with aplication of these libraries in pandas.
"""