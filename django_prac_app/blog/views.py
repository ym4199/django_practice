from django.contrib.auth import get_user_model
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostCreateForm

User=get_user_model()


# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {
        'title':'PostList from post_list view',
        'posts':posts,
    }
    return render(request, 'blog/post_list.html',context=context)


def post_detail(request,pk):
    # print('post_detail pk:',pk)
    # post 라는 키값으로 pk또는 id 값이 매개변수로 주어진 pk변수와 같은 post객체를 전
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("Question does not exist")
    context={
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html',{'post':post})




def post_create(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
            'form':form,
        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = User.objects.first()
            post = Post.objects.create(
                title=title,
                text=text,
                author = user
            )
        # return redirect('post_detail', pk=post.pk)
        return redirect('post_list')
    else:
        context={
            'form':form,
        }
        return render(request, 'blog/post_create.html',context)

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_list')


def post_modify(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostCreateForm()
    return render(request, 'blog/post_modify.html', {'form': form})