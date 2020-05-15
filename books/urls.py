from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    BookListView,
    UploadBookView
)


urlpatterns = [
    path('',views.home, name='book-home'),
    path('upload/',views.upload,name='book-upload'),
    path('books/',views.book_list,name='book-list'),
    path('books/upload/',views.upload_book,name='upload-book'),
    path('class/books/',BookListView.as_view(),name='class-book-list'),  #views.BookListView.as_view()
    path('class/books/upload',UploadBookView.as_view(),name='class-upload_book')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)