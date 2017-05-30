from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {
        'title':'PostList from post_list view',
        'posts':posts,
    }
    return render(request, 'blog/post_list.html',context=context)


def post_detail(request,pk):
    print('post_detail pk:',pk)
    # post 라는 키값으로 pk또는 id 값이 매개변수로 주어진 pk변수와 같은 post객체를 전
    context={
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html',context)


