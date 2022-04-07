import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "1.csv"
with open(filename) as f_obj:
    #利用csv.reader()这个方法，并且传参到其中，创建一个与该文件相关联的阅读器（reader）对象
    #并且将这个阅读器对象储存到reader里。
    reader =csv.reader(f_obj)
    #next(),返回文件中的下一行，因为下面调用了一次，所以只调用了一行
    header_row = next(reader)
    
    #enumerate()获取他的索引以及其值
    for index,column_header in enumerate(header_row):
        print(index,column_header)

    dates,highs,lows = [],[],[]
    
    for row in reader:
        #防止数据出错
        try:
            date = datetime.strptime(row[0],'%d/%m/%Y')
            high = float(row[2])
            low = float(row[3])    
        except ValueError:
            print(date,"missing data")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    fig = plt.figure(dpi=128,figsize=(10,6))
    
    plt.plot(dates,highs,c='red')
    plt.plot(dates,lows,c='blue')
    plt.fill_between(dates,highs,lows,facecolor='yellow',alpha=0.5)
    plt.title('Daily temperature, June 2020',fontsize=24)
    plt.xlabel('Days',fontsize=16)
    #让x轴坐标不重叠
    fig.autofmt_xdate()
    plt.ylabel('Temperature(℃)',fontsize=16)
    #which指的是主刻度，次刻度，还有二者major，minor，both
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.axis([dates[-1],dates[0],5,35])
    plt.show()
    