import csv
from matplotlib import pyplot as plt
from datetime import datetime

#从文件中获取最高温度和日期
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates = [],[]
    for row in reader:
        highs.append(int(row[1]))
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)




#根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

#设置图形的格式
plt.title("Dally high tempuratures",fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperture(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
