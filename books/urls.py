from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name='book-home'),
    path('upload/',views.upload,name='book-upload'),
    path('books/',views.book_list,name='book-list'),
    path('books/upload/',views.upload_book,name='upload-book')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)