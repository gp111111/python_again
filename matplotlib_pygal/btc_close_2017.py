import json
import pygal
import math
from itertools import groupby

filename = 'btc_close_2017_.json'
with open(filename) as f:
    btc_date = json.load(f)

dates =[]
months = []
weeks = []
weekdays = []
close = []
#打印每一天的信息
for btc_dict in btc_date:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = 'Closes ($)'
line_chart.x_labels = dates
N = 20 #坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('close price',close_log)
line_chart.render_to_file('close price ($).svg')

def draw_line(x_data,y_data,title,y_legend):
    xy_map = []

    #groupby分组函数，先把x_data和y_data对应，然后根据key来对x，y进行分类，key把元组的第一个元素作为分类标准进行分类
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart