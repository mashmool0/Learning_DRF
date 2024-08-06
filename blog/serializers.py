from rest_framework import serializers
from .models import Article


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50)
#     Text = serializers.CharField(max_length=300)
#     description = serializers.CharField(max_length=100)
#
#     def create(self,validate_data):
#         return Article.objects.create(**validate_data)
#


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "Text", "description")
        read_only_fields = ['description']
