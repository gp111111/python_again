from re import M
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#执行Web API调用,返回数据并存储响应
#sort=star意思是按照stars来进行排序
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("Status code:", r.status_code)
#将API响应存储在一个变量中
response_dict = r.json()
#处理结果
print(response_dict.keys())
print("Total respositories: ", response_dict['total_count'])

#探索有关仓库的信息
repo_dicts= response_dict['items']

names, stars, plot_dicts = [], [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict= {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)

#可视化
my_style = LS("#333366",base_style=LCS)
#定制图片的一些属性
my_config = pygal.Config() #创建属性实例
my_config.x_label_rotation = 45 
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size =18 #主标签更大，和副标签区分开
my_config.truncate_label = 15   #这个是将较长的字符缩短成15个字符，如果将鼠标指向该项目名，可显示完整名字
my_config.show_y_guides = False #隐藏图中的水平线
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style) #legend图例
chart.title = 'Most-starred Python Project on Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file("Python_repo.svg")
