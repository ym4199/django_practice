from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter()
    context = {
        'title':'PostList from post_list view',
        'posts':posts,
    }
    return render(request, 'blog/post_list.html',context=context)


