import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取最高温度、最低温度和日期
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []
    for row in reader:
        #对数据中的缺失情况进行处理
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)



#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图形的格式
plt.title("Dally high and low tempuratures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperture(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig("tempuratures.png")
plt.show()

