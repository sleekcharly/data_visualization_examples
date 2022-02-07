import csv
from datetime import datetime

from matplotlib import pyplot as plt

#  Get dates, high and low temperatures from file
filename = 'death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[6])
            low = int(row[7])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)        
            lows.append(low)

    # Plot data.
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title("Daily high and low Temperatures - 2018\nDeath valley, CA", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()