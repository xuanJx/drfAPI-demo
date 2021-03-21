from DragonOathApp import api_views

from rest_framework.routers import DefaultRouter

app_name = 'dragonapi'

urlpatterns = [

]

router = DefaultRouter()
router.register('users', api_views.UserViewSet, basename='users')
router.register('author', api_views.AuthorViewSet, basename='author')
router.register('apibooks', api_views.BooksViewSet, basename='books')
router.register('mark', api_views.MarkViewSet, basename='mark')
router.register('foreignAuthor', api_views.ForeignAuthorViewSet, basename='foreignAuthor')
router.register('pageview', api_views.PageViewModelViewSet, basename='pageView')
router.register('holmes', api_views.HolmesViewSet, basename='holmes')

urlpatterns += router.urls

# urlpatterns = [
#     url(r'^users/$', views.UserViewSet.as_view({"get": "list", "post": "create"}))
# ]