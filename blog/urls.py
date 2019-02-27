from django.urls import path
from .views import blog_list,Blog_detail
urlpatterns = [
    path('',blog_list,name='list'),
    path('<str:slug>/',Blog_detail.as_view(),name='blog_detail'),
    # path('<int:id>/',blog_detail,name='detail')
]
