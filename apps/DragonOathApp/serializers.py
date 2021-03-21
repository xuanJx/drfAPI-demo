from rest_framework import serializers
from apps.DragonOathApp.models import (Userinfo, Roleinfo, Author, BooksInfo, Mark, ForeignAuthor, Pageview,
                                       Holmes)

class HolmesViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holmes
        fields = '__all__'

class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pageview
        fields = '__all__'

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BooksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksInfo
        fields = '__all__'

class MarkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'

class ForeignAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignAuthor
        fields = '__all__'
