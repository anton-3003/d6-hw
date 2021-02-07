from django.urls import path
from .views import AuthorList, AuthorEdit, author_create_many, book_author_create_many
from p_library import views

app_name = 'p_library'
urlpatterns = [
    path('', views.main_page),
    path('author/create/', AuthorEdit.as_view(), name='author_create'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', book_author_create_many, name='book_author_create_many'),
]
