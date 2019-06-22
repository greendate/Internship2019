from django.urls import path
from . import views


urlpatterns = [
    path('', views.comments_list, name='comments_list'),
    path('new/', views.new_comment, name='new'),
    path('comment/<int:identify>/', views.comment, name='comment'),
    path('author/', views.comments_list, name='empty_author'),
    path('author/<str:username>/', views.author, name='author'),
]
