from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls')),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
