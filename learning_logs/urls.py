# defines url patterns for learning_logs

from django.urls import path
from . import views
#from . import learning_logs
# dot tells python to import views.py module from same directory as the current urls.py module
 
 
# app_name helps django distnguish this* urls.py file from files of the same name in other apps within the project
app_name = 'learning_logs'
# var below is a list of individual pages tht can be reqstd from learning_logs app 
urlpatterns = [
# home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name ='new_entry'),
    # for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    

]

# detail page for a single topic 
path('topics/<int:topic_id>/', views.topic, name='topic')


# page that shows all topics
#path('topics/', views.topics, name='topics')







