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


class UpdateArticleView(APIView):
    def put(self, request, pk):
        # Set partial to True for change just one element in database
        instance = Article.objects.get(id=pk)
        ser = ArticleSerializer(instance=instance, data=request.data, partial=True)
        if ser.is_valid():
            ser.update(instance, ser.validated_data)
            return Response({"message": "Changed"})
        else:
            return Response(ser.error_messages)

    def delete(self, request, pk):
        if Article.objects.filter(id=pk).exists() :
            instance = Article.objects.get(id=pk)
            instance.delete()
            return Response({"message": "Deleted"})
        else : return Response({"message":"We dont have this Article id in data base"})


def blog_view(request):
    article = Article.objects.all()
    return render(request, "blog/index.html", context={"articles": article})
