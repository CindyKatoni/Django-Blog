from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Welcome To The Blog'
    return render(request, 'blog/home.html', {'title':title})

def about(request):
     title = 'About'
     return render(request, 'blog/about.html', {'title':title})   