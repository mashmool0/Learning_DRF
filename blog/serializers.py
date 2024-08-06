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

    # def validate_title(self, value):
    #     if value == "Html":
    #         raise serializers.ValidationError("You can't choose Html")
    #     else:
    #         return value

    def validate(self, attrs):
        if attrs['title'] == attrs['Text']:
            raise serializers.ValidationError("title and text can not be same!!!!")
        return attrs

