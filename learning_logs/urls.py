"""定义learning_logs的URL模式"""
from django.urls import path
from django.conf.urls import url
from . import views

# app_name = 'learning_logs'  #这个属性在html模板中用来指定命名空间：

urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^$', views.index, name='index'),
    # path('topics', views.topics, name='topics'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]

