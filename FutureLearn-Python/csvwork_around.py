##import os
##import matplotlib.pyplot as plt
##import csv
##
### os.chdir('C:\\Users\Ayobami Haastrup\Desktop')
##salesdata = []
##with open('company_sales_data.csv', 'r') as f:
##    reader = csv.DictReader(f)
##    for row in reader:
##        salesdata.append(row)
##
##xvalue = [k for k in salesdata[0].keys()]
##yvalue = [v for v in salesdata[0].values()]
##
##plt.style.use('seaborn')
##fig, ax = plt.subplots()
##ax.plot(xvalue, yvalue, linewidth = 2)
###plt.scatter(xvalue, yvalue)
##plt.show()
####    for sales in salesdata:
####        for key in sales.keys():
####            print(f"{key}")
##
####    for sales in salesdata:
####        for key, value in sales.items():
####            print(f"{key} : {value}")
##
####print(len(sales))
####print(len(sale))
##
##        
####
####plt.style.use('classic')
####fig, ax = plt.subplots()
####plt.scatter(x_values, y_values)
##### Remove the axes.
####ax.get_xaxis().set_visible(False)
####ax.get_yaxis().set_visible(False)
####
####
####
##### Show plot.
####plt.show()
####
##### Save plot
##### plt.savefig(choice(alphabs), bbox_inches= 'tight')
####keep_up = input('Do you want to make another walk (y/n)?: ')
####if keep_up.lower() == 'n':
####break


#Parsing CSV File Headers#
from matplotlib import pyplot as plt
from datetime import datetime
import csv

highs, lows, dates, highs_lows = [], [], [], []
filename = 'two_month_temp_finland.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column in enumerate(header_row):
        print(index, column)

        
    # get high and low temperature
    # Get date 
    for row in reader:
        #print(row[12])
        high = row[6]
        low = row[7]
        current_date = datetime.strptime(row[5], '%d/%m/%Y')
        high_low = high + low
        
        lows.append(low)
        highs.append(high)
        dates.append(current_date)
        highs_lows.append(high_low)

# Plot highs
plt.style.use('seaborn')
fig, ax = plt.subplots()
#date_part, highs_part, lows_part = len(dates) // 3,  len(highs) // 3, len(lows) // 3
ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
##ax.plot(dates, highs_lows, c='blue', alpha=0.3)
##plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1) 

# Format plot.
plt.title(f"Daily highs and low temperatures -  01/JAN/2020 -  01/MAR/2020", fontsize=20)
plt.xlabel('Month', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
plt.show()
