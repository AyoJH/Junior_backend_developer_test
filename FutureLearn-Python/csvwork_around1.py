from matplotlib import pyplot as plt
from datetime import datetime
import csv

highs, lows, dates = [], [], []

filename = 'two_month_temp_finland.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
##    for index, column in enumerate(header_row):
##        print(f"{index}':'{column}")

        
    # get high and low temperature
    # Get date 
    for row in reader:
        #print(row[12])
        high = row[6]
        low = row[7]
        current_date = datetime.strptime(row[5], '%d/%m/%Y')
        lows.append(low)
        highs.append(high)
        dates.append(current_date)
        

plt.style.use('seaborn')
fig, ax = plt.subplots()
##sorted_lows, sorted_highs, sorted_dates = sorted(lows), sorted(highs), sorted(dates)
ax.plot(dates, lows, c='blue', alpha=0.3)
##ax.plot(dates, highs, c='red', alpha=0.3)
##ax.scatter(dates, lows, c='green', alpha=0.3)
##ax.scatter(dates, highs, c='black', alpha=0.3)


#ax.plot(sorted_dates, sorted_highs, c='red', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)
plt.title(f"Daily highs and low temperatures -  01/JAN/2020 -  01/MAR/2020", fontsize=20)
plt.xlabel('Month', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
plt.xlabel('Month', fontsize=10)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=10)
print(lows)
print(len(lows))
print(len(highs))
print(len(dates))
plt.show()


