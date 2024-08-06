from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    datetime = serializers.DateTimeField()