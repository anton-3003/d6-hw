from django.urls import path
from .views import AuthorList, AuthorAdd, author_create_many, book_author_create_many, FriendAdd, BookEdit, BookDelete, BookAdd, PublisherCreate
from p_library import views

app_name = 'p_library'
urlpatterns = [
    # path('', views.main_page, name='main_page'),
    path('', views.index, name='index'),
    path('author/create/', AuthorAdd.as_view(), name='author_create'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/create_many/', author_create_many, name='author_create_many'),
    path('author_book/create_many/', book_author_create_many, name='book_author_create_many'),
    path('friend/add/', FriendAdd.as_view(), name='friend_create'),
    path('friend_list/', views.friends, name='friends'),
    path('book/create/', BookAdd.as_view(), name='book_add'),
    path('book/<int:pk>/', BookEdit.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', BookDelete.as_view(), name='book_delete'),
    path('publisher/', views.publishers, name='publishers'),
    path('publisher/create/', PublisherCreate.as_view(), name='pulisher_add')
]
