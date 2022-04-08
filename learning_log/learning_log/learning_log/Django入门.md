D现在网站实际上都是富应用程序(rich application),像成熟的桌面程序一样app，学习使用Django来进行网站的开发
为这个项目制定规范，然后为应用程序使用的数据定义模型，使用Django的管理系统来输入一些初始数据再学习编写视图和模版。

Django是一个web框架，一套用于帮助开大交互式网站的工具。Django能响应网页的请求，更轻松读写数据，管理用户，后面还会部署到服务器。

建立项目时，需要以规范的方式对项目进行描述，再建立**虚拟环境**，以便在其中创建项目。
（Python虚拟环境的主要目的是为了给不同的工程创建互相独立的运行环境。在虚拟环境下，每一个工程都有自己的依赖包，而与其它的工程无关。不同的虚拟环境中同一个包可以有不同的版本。并且，虚拟环境的数量没有限制，我们可以轻松地用virtualenv或者pyenv等工具来创建多个虚拟环境。）

# 建立虚拟环境
要使用Django，需要先建立一个虚拟的工作环境。虚拟环境是系统的一个位置，可以在其中安装包，并且和其他的包隔离，将项目的库与其他项目的库分离开是有益的，而且部署到服务器上的时候也是必须的。
# 创建项目
django -admin.py startproject learning_log.
manage.py的文件是一个简单的程序，接受命令并将其交给Django的相关部分去运行。我们将使用这些命令来管理使用数据库和运行服务器等任务
setting.py是指定Django如何与你的系统交互以及如何管理项目，在开发的过程修改设置，并且添加一些设置。文件urls.py告诉Django应该创建哪些网页来响应浏览器请求。文件wsgi.py帮助Django提供它创建的文件，这个文件名是缩写，wed server gateway interface（web服务器网关接口）

# 创建数据库
mange.py migrate
我们将修改数据库称为迁移数据库，首次执行migrate命令时，将让Django确保数据库与项目的当前状态匹配，在使用SQLite的新项目中首次执行这个命令时，Django将新建一个数据库。
在输出Django指出它将创建必要的数据库表，用于存储我们将在这个项目中使用的信息（synchronize unmigrated apps同步未迁移的应用程序），再确保数据库结构与当前代码（Apply all migrations应用所有迁移）匹配
创建了一个新的文件db.sqlite3。SQLite是一种使用单个文件的数据库，是编写简单应用程序的理想选择，因为它让你不用太关注数据库的管理问题。
# 查看项目
python manage.py runsever
Django启动一个服务器，让你能够查看系统中的项目，了解其工作情况，在浏览器中输入url以请求网页时，Django服务器将进行响应，生成合适的网页发送给浏览器。
输出指出Django检查正确创建了项目，Django版本，项目的[http://127.0.0.1:8000/](http://127.0.0.1:8000/)表明项目将在你的计算机，也就是localhost的端口8000上侦听请求。localhost是一种只处理当前系统发出的请求，而不予许其他任何人查看正在开发的网页服务器

# 创建应用程序
Django项目由一系列应用程序组成，它们协同工作，让项目成一个整体。我们暂时只创建一个应用程序，他将完成大部分工作。
命令startapp _appname_让Django创建应用程序所需的基础设施。，新增了一个appname的文件夹，最重要的文件是model.py定义在应用程序中要管理的数据，admin.py和views.py后面介绍
## 定义模型
每位用户在学习笔记中创建很多主题，输入的每个条目与特定主题相关联，这些条目将以文本的方式显示，需要存储每个条目的时间戳，以便告诉用户各个条目是何时创建的
## 激活模型
要使用模型，必须让Django将应用程序包含到项目中，为此打开settings.py,installed_apps告诉那些应用程序安装在项目中，将我们创建的应用程序也添加进去。
通过将应用程序编组，在项目不断扩大，包含更多的应用程序时，有助于对应用程序进行跟踪。
然后利用终端修改数据库，让他能够存储与模型Topic相关的信息，![截屏2022-04-08 14.12.58.png](https://cdn.nlark.com/yuque/0/2022/png/23131853/1649398384396-0af2a7ba-5090-4a1e-bfce-e65895f1095b.png#clientId=u2de1197d-dc2d-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=udc6f794b&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2022-04-08%2014.12.58.png&originHeight=142&originWidth=1128&originalType=binary&ratio=1&rotation=0&showTitle=false&size=31949&status=done&style=none&taskId=u9da4138c-9645-4285-987b-e404be17e01&title=)
makemigrations appname让Django确定该如何修改数据库，让其能够存储我们定义的新模型相关联的数据。输出表明Django创建了一个名是0001_initial.py的迁移文件，这个文件将在数据库中为模型Topic创建一个表
然后应用这种迁移，让Django替我们修改数据库
![截屏2022-04-08 14.20.23.png](https://cdn.nlark.com/yuque/0/2022/png/23131853/1649398829058-ddce7e96-9570-4423-bb8e-23786fbc8702.png#clientId=u2de1197d-dc2d-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uf3da80dd&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2022-04-08%2014.20.23.png&originHeight=170&originWidth=1054&originalType=binary&ratio=1&rotation=0&showTitle=false&size=43674&status=done&style=none&taskId=u5587f210-f991-4fe1-b021-3ba0cf082d2&title=)
要检查的是OK这一行。
每当需要修改学习笔记管理的数据时，都采取如下三个步骤，修改model.py，对learning_logs调用makemigrations；让Django迁移项目
## Django管理网站
admin site管理网站轻松处理模型，管理员可使用管理网站，但普通用户不能
### 创建超级用户
Django允许你创建具备所有权限的用户——超级用户。权限决定了用户可执行的操作，最严格的权限设置只允许用户阅读网站的公开信息，注册了的用户通常可以阅读自己的私有数据，还可以查看一些只有会员才能查看的信息，为了有效管理web应用程序，网站所有者通常需要访问网站存储的所有信息，小心管理敏感信息![截屏2022-04-08 14.44.17.png](https://cdn.nlark.com/yuque/0/2022/png/23131853/1649400263024-5457ee92-d4b3-4fc5-b296-b8f5214b00c8.png#clientId=u2de1197d-dc2d-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uf2a13db2&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2022-04-08%2014.44.17.png&originHeight=138&originWidth=1092&originalType=binary&ratio=1&rotation=0&showTitle=false&size=33117&status=done&style=none&taskId=ucd6937d9-469e-457d-bb5e-f5fcb513967&title=)
### 向管理网站注册模型
Django自动在管理网站中添加了一些模型，User和Group，但我们创建的模型必须手工注册
注册了topic模型，topic是我们在model.py里自己写入的模型
## 添加主题
直接网页add就行
## 定义模型Entry
记录关于topic的知识，需要为用户可在学习笔记中添加的条目定义模型，每个条目都与特定主题相关联，这种对应关系就是多对一关系，即多个条目可关联到同一个主题。
外键是一个数据库术语，它引用了数据库中的另一条记录；这些代码将每个条目关联到特定的主题。每个主题创建时，都给他分配了一个键（ID）。需要在两项数据之间建立联系时，Django使用与每项信息相关联的键。稍后我们将根据这些联系获取与特定主题相关联的所有条目。
并且嵌套了meta类，meta存储用于管理模型的额外信息。在这里让我们设置一个特殊属性，让Django在需要时使用Entries来表示多个条目。如果没有这个类，将使用Entrys表示多个条目。
__str_表示让Django只显示text的前50个字符。
## 迁移模型Entry
生成新的迁移文件——0002_entry.py，他告诉Django如何修改数据库，式其能够存储与模型Entry相关的信息。
## 向管理网站注册Entry
admin.site.register(Entry)
## Django shell
输入一些数据后，可以通过交互式终端会话以编程方式查看这些数据。这种交互式环境称为Django shell，是测试项目和排除其故障的理想之地![截屏2022-04-08 18.32.56.png](https://cdn.nlark.com/yuque/0/2022/png/23131853/1649413980252-a00b5396-141b-4eec-8ec8-b7240ac81c67.png#clientId=u2de1197d-dc2d-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=u3eaba9c4&margin=%5Bobject%20Object%5D&name=%E6%88%AA%E5%B1%8F2022-04-08%2018.32.56.png&originHeight=364&originWidth=1130&originalType=binary&ratio=1&rotation=0&showTitle=false&size=53632&status=done&style=none&taskId=ued873b84-8a9b-44d1-b598-a6a6d87502d&title=)
通过外键关系获取数据，可使用相关模型小写名称，下划线，和单词set.all(）
# 创建网页：学习笔记主页
使用Django创建网页一般分为三个阶段：定义URL，编写视图和编写模版。
首先必须定义URL模式。URL模式描述了URL是如何设计的，让Django知道如何将浏览器请求与网站RURL匹配，已确定返回那个网页

每个URL都被映射到特定的视图-视图函数获取并处理网页所需的数据，视图函数通常调用一个模版。
