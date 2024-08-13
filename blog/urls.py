from django.urls import path
from . import views

name_app = "blog"
urlpatterns = [
    path('blogList', views.ListBlogsView.as_view(), name="blogListView"),
    path('blogAdd', views.AddArticleView.as_view(), name="blogAddView"),
    path('blogName', views.NameBlogsView.as_view(), name="blogNameView"),
    path('blogUpdate/<str:pk>', views.UpdateArticleView.as_view(), name="blogUpdateView"),
    path('check', views.CheckToken.as_view(), name="CheckTokenView"),
    path('', views.blog_view, name="blogView"),
]
