from django.shortcuts import render
from rest_framework.views import APIView
from .models import Article
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import ArticleSerializer


# Create your views here.


class ListBlogsView(APIView):
    def get(self, request):
        instance = Article.objects.all()
        ser = ArticleSerializer(instance=instance, many=True)
        return Response(data=ser.data)


class AddArticleView(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Added"})


def blog_view(request):
    article = Article.objects.all()
    return render(request, "blog/index.html", context={"articles": article})
