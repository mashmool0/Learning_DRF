from django.urls import path
from . import views

name_app = "blog"
urlpatterns = [
    path('blogList', views.ListBlogsView.as_view(), name="blogListView"),
    path('blogAdd', views.AddArticleView.as_view(), name="blogAddView"),
    path('blogUpdate/<str:pk>', views.UpdateArticleView.as_view(), name="blogUpdateView"),
    path('', views.blog_view, name="blogView"),
]
