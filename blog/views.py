from django.shortcuts import render
from rest_framework.views import APIView
from .models import Article
from rest_framework.response import Response
from django.views.generic import TemplateView
from .serializers import ArticleSerializer, ArticleSerializerName
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

class NameBlogsView(APIView):
    def get(self, request):
        instance = Article.objects.all()
        ser = ArticleSerializerName(instance=instance, many=True)
        return Response(data=ser.data)


class ListBlogsView(APIView):
    def get(self, request):
        instance = Article.objects.all()
        ser = ArticleSerializer(instance=instance, many=True)
        return Response(data=ser.data)


# class AddArticleView(APIView):
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             if request.user.is_authenticated:
#                 serializer.validated_data['user'] = request.user
#
#             serializer.save()
#             return Response({"message": "Added"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)

class AddArticleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.validated_data['user'] = request.user

            serializer.save()
            return Response({"message": "Added"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


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
        if Article.objects.filter(id=pk).exists():
            instance = Article.objects.get(id=pk)
            instance.delete()
            return Response({"message": "Deleted"})
        else:
            return Response({"message": "We dont have this Article id in data base"})


class CheckToken(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        user = request.user
        return Response({"user": user.username}, status=status.HTTP_200_OK)


def blog_view(request):
    article = Article.objects.all()
    return render(request, "blog/index.html", context={"articles": article})
