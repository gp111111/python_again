#定义learning_logs的URL模式
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    #主页
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topic/<topic_id>', views.topic,name='topic')
]

app_name = 'Learning_logs'