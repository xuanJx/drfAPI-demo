from django.urls import path
from DragonOathApp import views

app_name = 'dragonapp'

urlpatterns = [
    path('login/', views.login_view, name='login-page'),
    path('register/', views.register_view, name='register-page'),
    path('index/', views.index_view, name='index-page'),
    path('authors/', views.authors_view, name='authors-page'),
    path('author/<int:pk>/', views.author_view, name='author-page'),
    path('books/', views.books_view, name='books-page'),
    path('book/<int:pk>/', views.book_view, name='book-page'),
    path('foreignAuthor/', views.foreign_author, name='foreignAuthor-page'),
    path('test/', views.test, name='test-page'),
    path('holmes/', views.holmes_view, name='holmes-page'),
    path('holmes/<int:pk>/', views.holmes_view_pk, name='holmes-pk-page'),
    path('original/', views.original_view, name='original-page')
]

