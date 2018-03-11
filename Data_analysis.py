
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("EbayData.csv")


instance_count, attr_count = data.shape

print( "Pricing")

df = data["price"]

print( df.describe() )

print("Rating")

df2 = data["rating"]

print( df2.describe() )



# get the maximum  and minimum length strings in the name 
# column in the csv table

for i in data:

      # if the type of the elements is a string get the size 
      # and display the lowest and highest string sizes
      if data[i].dtype == 'object':
          
         print(" Max %s: %s\n",  (i, data[i].map(len).max()))
         print(" Min %s: %s\n",  (i, data[i].map(len).min()))



print( " Build Histogram for data analysis ")

#  Build histogram for data analysis  

histo1 = data['rating']
 
histo2 = data['price']

histo3 = data['name'].map(len)

# Histogram for the rating column from the csv table
plt.hist( histo1, normed=True, bins='auto')
plt.ylabel('Rating Frequency in the  dataset')
plt.xlabel('Rating Range')
plt.title('Rating Histogram')

# Histogram for price column from the csv table
# plt.hist( histo2, normed=True, bins='auto')
# plt.ylabel('Price Frequency in the  dataset')
# plt.xlabel('Pricing Range')
# plt.title('Pricing Histogram')


# Histogram for string length in the name column in the csv table
# plt.hist(histo3, normed=True, bins='auto')
# plt.ylabel('Frequence of Video Games Name')
# plt.xlabel('Game names length Range ')
# plt.title('Video Games Name Histogram')

plt.show()



