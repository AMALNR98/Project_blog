from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
    # return HttpResponse('<h1>Blog Home<h1>')

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
    # return HttpResponse("<h1>Blog About</h1>")



    #superUser : amalNR
    #pw        : z55ultra











    # posts = [
#     {
#         'author' : 'CoreyMs',
#         'title' : 'Blog post 1',
#         'content':'First post content',
#         'date_posted':'December 21, 2022'
#     },
#     {
#         'author' : 'jane',
#         'title' : 'Blog post 2',
#         'content':'Second post content',
#         'date_posted':'December 21, 2022'
#     },
#     {
#         'author' : 'CoreyM',
#         'title' : 'Blog post 3',
#         'content':'Third post content',
#         'date_posted':'December 21, 2022'
#     },
# ]