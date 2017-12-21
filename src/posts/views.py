from django.shortcuts import render, redirect
from .models import Post, Comments
from .forms import CommentForm, PostForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def show_posts(request, number=1):
    template_name = 'posts.html'
    all_posts = Post.objects.all()

    query = request.GET.get("q")
    if query:
        all_posts = all_posts.filter(Q(title__icontains=query) | Q(body__icontains=query)).distinct()
    
    current_page = Paginator(all_posts, 6)
    args = {
        'posts': current_page.page(number),
    }
    return render(request, template_name, args)


@login_required
def get_post(request, id, number=1):
    template_name = 'detail_post.html'
    post_details = Post.objects.get(id=id)
    comments = Comments.objects.filter(comment_post_id = id)
    current_page = Paginator(comments, 10)

    form = CommentForm
        
    args = {
        'post': post_details,
        'comments': current_page.page(number),
        'form': form,

    }
    return render(request, template_name, args)

@login_required
def create_post(request):
    template_name = 'create_post.html'
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/posts')
    
    args = {
        'form': form,
    }

    return render(request, template_name, args)


@login_required
def add_comment(request, id):
    if request.method == "POST":
        form  = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = Post.objects.get(id = id)
            form.save()
    return redirect('/posts/post/%s/' %id)

@login_required
def about(request):
    template_name = 'about.html'
    return render(request, template_name, {})

