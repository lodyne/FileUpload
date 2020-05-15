from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import (
    ListView,
    CreateView
)
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book
# Create your views here.
def home(request):
    return render(request,'books/home.html')


# How to handle file upload without model forms
def upload(request):
    # Files must be sent using POST request
    if request.method == 'POST':  
        ''' Files uploaded are dictionary-like object and the key must be
        *name of the file input* that was added in html i.e document '''

        uploaded_file= request.FILES['document'] 
        # print(uploaded_file.name)
        # print(uploaded_file.size)

        # To handle files, use File storage API i.e FileSystemStorage
        file=FileSystemStorage()

        # Each file uploaded as dictionary are going to be UploadedFile instance
        name=file.save(uploaded_file.name,uploaded_file)

        url =file.url(name)
    

    # context={
    #     'url' : url
    # }

    return render(request,'books/upload.html')

def book_list(request):
    context = {
        'books':Book.objects.all()
    }
    return render(request, 'books/book_list.html',context)
    

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form=BookForm()
        
    context={
        'form':form
    }
    
    return render(request, 'books/upload_book.html',context)

class BookListView(ListView):
    model = Book
    template_name = 'books/class_book_list.html'
    context_object_name = 'books'

class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    # fields = '__all__' 
    success_url = reverse_lazy('class-book-list')
    template_name = 'books/upload_book.html'



