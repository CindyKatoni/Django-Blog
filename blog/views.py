from django.shortcuts import render
 
posts = [
    {
        'title': 'Blog Post 1',
        'author': 'Cindy Kat',
        'content': 'Im a software developer',
        'date_posted': 'July 20, 2021'
    },
    {
         'title': 'Blog Post 2',
        'author': 'Lucy Kamene',
        'content': 'Im a penetration tester',
        'date_posted': 'July 20, 2021'
    }
]

# Create your views here.
def index(request):
    
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
     return render(request, 'blog/about.html', {'title':'About'})   