from apps.DragonOathApp.models import Userinfo, Roleinfo, Author, BooksInfo, ForeignAuthor, Mark, Pageview, Holmes
from apps.DragonOathApp.serializers import (
    UserModelSerializer, AuthorModelSerializer, BooksModelSerializer, HolmesViewSerializer,
    MarkModelSerializer, ForeignAuthorSerializer, PageViewSerializer,
)
from rest_framework.viewsets import ModelViewSet

class HolmesViewSet(ModelViewSet):
    queryset = Holmes.objects.all()
    serializer_class = HolmesViewSerializer

class UserViewSet(ModelViewSet):
    queryset = Userinfo.objects.all()
    serializer_class = UserModelSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class BooksViewSet(ModelViewSet):
    queryset = BooksInfo.objects.all()
    serializer_class = BooksModelSerializer

class MarkViewSet(ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkModelSerializer

class ForeignAuthorViewSet(ModelViewSet):
    queryset = ForeignAuthor.objects.all()
    serializer_class = ForeignAuthorSerializer

class PageViewModelViewSet(ModelViewSet):
    queryset = Pageview.objects.all()
    serializer_class = PageViewSerializer
