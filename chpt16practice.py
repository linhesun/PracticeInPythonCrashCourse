# Chapter 16 practice
# Linhe Sun

# practice 16-1
# we can not download the CSV file any more in the website

# practice 16-2
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
class HighLow():
    def __init__(self, filename):
        self.filename = filename
        self.dates = []
        self.highs = []
        self.lows =[]
    
    def extract_data(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    high = int(row[1])
                    low = int(row[3])
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    self.dates.append(current_date)
                    self.highs.append(high)
                    self.lows.append(low)

death_valley = HighLow('death_valley_2014.csv')
death_valley.extract_data()

sitka = HighLow('sitka_weather_2014.csv')
sitka.extract_data()

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(sitka.dates, sitka.highs, c='violet', alpha=0.5)
plt.plot(sitka.dates, sitka.lows, c='violet', alpha=0.5)
plt.fill_between(sitka.dates, sitka.highs, sitka.lows, facecolor='violet', alpha=0.1)


plt.plot(death_valley.dates, death_valley.highs, c='blue', alpha=0.5)
plt.plot(death_valley.dates, death_valley.lows, c='blue', alpha=0.5)
plt.fill_between(death_valley.dates, death_valley.highs, death_valley.lows, facecolor='blue', alpha=0.1)

plt.ylim(0,120)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley(Blue) & Sitka(Violet)"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# practice 16-3
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
class PrecipitationIn():
    def __init__(self, filename):
        self.filename = filename
        self.dates = []
        self.precipitation_ins = []
    
    def extract_data(self):
        with open(self.filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            for row in reader:
                try:
                    current_date = datetime.strptime(row[0], "%Y-%m-%d")
                    precipitation = float(row[19])
                except ValueError:
                    print(current_date, 'missing data')
                else:
                    self.dates.append(current_date)
                    self.precipitation_ins.append(precipitation)
                    

death_valley = PrecipitationIn('death_valley_2014.csv')
death_valley.extract_data()

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(death_valley.dates, death_valley.precipitation_ins, c='blue', alpha=0.5)

# Format plot.
title = "Daily Precipitation In - 2014\nDeath Valley"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# practice 16-4
# pass

# practice 16-5


# ## 16.2 制作比特币收盘价走势图：JSON 格式
# 在本节中，你将下载JSON格式的比特币（2009年由中本聪发明，
# 是一种去中心化、全球通用、基于区块链的电子加密货币，
# `https://bitcoin.org/zh_CN`）收盘价数据，并使用`json`模块来处理它们。
''' actually i can not open the website ---- Linhe Sun '''
# Pygal提供了一个适合初学者使用的绘图工具，可以用它对比特币收盘价数据进行可视化，以探索比特币价格的特征。

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
try:
    # Python 2.x 版本
    from urllib2 import urlopen
except ImportError:
    # Python 3.x 版本
    from urllib.request import urlopen  # 1
import json
import requests
import pygal
import math
from itertools import groupby


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)  # 2
# 读取数据
req = response.read()
# 将数据写入文件
with open('btc_close_2017_urllib.json', 'wb') as f:  # 3
    f.write(req)
# 加载json格式
file_urllib = json.loads(req.decode('utf8'))  # 4
print(file_urllib)


json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)  # 1
# 将数据写入文件
with open('btc_close_2017_request.json', 'w') as f:
    f.write(req.text)  # 2
file_requests = req.json()  # 3


print(file_urllib == file_requests)

btc_data = file_requests = req.json()
# 将数据加载到一个列表中
#filename = 'btc_close_2017.json'
# u should add "  ,'r',encoding='UTF-8' " or python can not read the file
#with open(filename,'r',encoding='UTF-8') as f:
    #btc_data = json.load(f)  # 1
# JSONDecodeError use the json file download from github (use chrome)
 

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))  # 1
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))


# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)  # ①
line_chart.title = '比特币收盘价（¥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]  # ②
line_chart.add('收盘价', close)
line_chart.render_to_file('比特币收盘价折线图（¥）.svg')


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '比特币收盘价对数变换（¥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]  # ①
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('比特币收盘价对数变换折线图（¥）.svg')
line_chart


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
    months[:idx_month], close[:idx_month], '比特币收盘价月日均值（¥）', '月日均值')
line_chart_month


idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(
    weeks[1:idx_week], close[1:idx_week], '比特币收盘价周日均值（¥）', '周日均值')
line_chart_week


idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday',
      'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(
    weekdays_int, close[1:idx_week], '比特币收盘价星期均值（¥）', '星期均值')
line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line_chart_weekday.render_to_file('比特币收盘价星期均值（¥）.svg')
line_chart_weekday


with open('比特币收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>比特币收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            '比特币收盘价折线图（¥）.svg', '比特币收盘价对数变换折线图（¥）.svg', '比特币收盘价月日均值（¥）.svg',
            '比特币收盘价周日均值（¥）.svg', '比特币收盘价星期均值（¥）.svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')
    
# practice 16-6
# i didn't find any interesting data in english on http://okfn.org/

# practice 16-7
import unittest
from btc_close_2017 import draw_line

class TestDrawLine(unittest.TestCase):
    
    def test_draw_linhe(self):
        x_data = ['a','b','a','b','c','c','d','d','e','e']
        y_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x_test = ['a','b','c','d','e']
        y_test = [2, 3, 5.5, 7.5, 9.5]
        test_chart = draw_line(x_data, y_data, 'Test Title', 'Test')
        self.assertEqual(test_chart.title, 'Test Title')
        self.assertEqual(test_chart.x_labels, x_test)
        #self.assertEqual(test_chart.values, y_test) -----this doesn't work, actually i dont know how to extract the values from the chart
        
unittest.main()

# practice 16-8
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
from numpy import *
print(eye(4))
