from django.urls import path
from . import views


urlpatterns = [
    path('', views.comments_list, name='comments_list'),
    path('new/', views.new_comment, name='new'),
]
