from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
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