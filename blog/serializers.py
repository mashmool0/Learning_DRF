from rest_framework import serializers
from .models import Article


# this is for first method
# def check_title(value):
#     if value == "html":
#         raise serializers.ValidationError("Title can't be html")


# this is for second method
def check_title(data):
    if data['title'] == "html":
        raise serializers.ValidationError("title can't be html ! please try another title <3 :) ")
        # raise serializers.ValidationError({"title Errors":"title can't be html ! please try another title <3 :) "})


class CheckTitle:

    def __call__(self, data):
        if data['title'] == 'html':
            raise serializers.ValidationError("Error title cant be html")

        # first method


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=50,validators=[check_title,or CheckTitle])
#     Text = serializers.CharField(max_length=300)
#     description = serializers.CharField(max_length=100)
#
#     def create(self,validate_data):
#         return Article.objects.create(**validate_data)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "Text", "description", "user")
        read_only_fields = ['description']
        validators = [check_title]

    # def validate_title(self, value):
    #     if value == "Html":
    #         raise serializers.ValidationError("You can't choose Html")
    #     else:
    #         return value

    def validate(self, attrs):
        if "Text" in attrs :
            if attrs['title'] == attrs['Text']:
                raise serializers.ValidationError("title and text can not be same!!!!")

        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data['user'] = request.user
        return Article.objects.create(**validated_data)


class ArticleSerializerName(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title",)
