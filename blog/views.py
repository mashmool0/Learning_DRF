from django.shortcuts import render
from rest_framework.views import APIView
from .models import Article
from rest_framework.response import Response
from django.views.generic import TemplateView


# Create your views here.


class ListBlogsView(APIView):
    def get(self, request):
        instance = Article.objects.all()
        articles = [item.title for item in instance]
        return Response(articles)


def blog_view(request):
    article = Article.objects.all()
    return render(request, "blog/index.html", context={"articles": article})
