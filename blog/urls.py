from django.urls import path
from . import views

name_app = "blog"
urlpatterns = [
    path('blogList', views.ListBlogsView.as_view(), name="blogListView"),
    path('', views.blog_view, name="blogView"),
]
