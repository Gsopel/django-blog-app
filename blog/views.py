from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages



def home(request):
    posts_list = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts_list, 3)

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'blog/home.html', {'posts': posts})
'''
def home(request):
    context = {
        'posts':Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    }
    return render(request, 'blog/home.html', context)
'''


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST" and request.user == post.author:
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST" and request.user == post.author:
        post.delete()
       # messages.success(request, "Post successfully deleted!")
        return redirect('blog_home')

    return render(request, 'blog/post_delete.html', {'post': post})

