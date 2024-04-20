from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment
from django.contrib import messages
from .utils import searchPosts, searchCategories
from .forms import PostForm, CommentForm, CategoryForm

# Create your views here.

def posts(request):
    posts, search = searchPosts(request)
    # posts = Post.objects.all()
    context = {
        "posts": posts,
        "search": search,
    }
    return render(request, "posts/posts.html", context)

# def post(request, pk):
#     postObj = Post.objects.get(id=pk)
#     context = {
#         'post': postObj
#     }
#     return render(request, 'posts/post.html', context)

def post(request, pk):
    post_obj = Post.objects.get(id=pk)
    comments = post_obj.comments.filter(parent=None)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user.profile
            comment.post = post_obj
            parent_id = comment_form.cleaned_data.get('parent_id')
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
                comment.parent = parent_comment
            comment.save()
            return redirect('post', pk=pk)
    else:
        comment_form = CommentForm()

    context = {
        'post': post_obj,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'posts/post.html', context)

def categories(request):
    categories, search = searchCategories(request)
    # categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'posts/categories.html', context)

def category(request, pk):
    page = 'category'
    category = Category.objects.get(id=pk)
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts,
        'category': category,
        'page': page
    }
    return render(request, 'posts/posts.html', context)

@login_required(login_url="login")
def createPost(request):
    profile = request.user.profile
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # profile = Profile.objects.get(user=request.user)
            post = form.save(commit=False)
            post.owner = profile
            post.save()
            return redirect('posts')

    context = {
        'form': form
    }
    return render(request, 'posts/post_form.html', context)

@login_required(login_url="login")
def updatePost(request, pk):
    profile = request.user.profile
    post = profile.post_set.get(id=pk)

    form = PostForm(instance=post)

    if request.method == 'POST':
        # print(request.POST)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {
        'form': form
    }
    return render(request, 'posts/post_form.html', context)

@login_required(login_url="login")
def deletePost(request, pk):
    profile = request.user.profile
    post = profile.post_set.get(id=pk)

    if request.user != post.owner.user:
        return redirect('permission_denied')

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    context = {
        'object': post
    }
    return render(request, 'posts/delete_template.html', context)

@login_required(login_url="login")
def createCategory(request):
    profile = request.user.profile
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # profile = Profile.objects.get(user=request.user)
            category = form.save(commit=False)
            category.owner = profile
            category.save()
            return redirect('categories')

    context = {
        'form': form
    }
    return render(request, 'posts/category_form.html', context)

@login_required(login_url="login")
def updateCategory(request, pk):
    profile = request.user.profile
    category = profile.category_set.get(id=pk)

    form = CategoryForm(instance=category)

    if request.method == 'POST':
        # print(request.POST)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    context = {
        'form': form
    }
    return render(request, 'posts/category_form.html', context)

@login_required(login_url="login")
def deleteCategory(request, pk):
    profile = request.user.profile
    category = profile.category_set.get(id=pk)

    if request.user != category.owner.user:
        return redirect('permission_denied')

    if request.method == 'POST':
        category.delete()
        return redirect('categories')

    context = {
        'object': category
    }
    return render(request, 'posts/delete_template.html', context)

@login_required(login_url="login")
def likePost(request, pk):
    post = Post.objects.get(id=pk)
    user_profile = request.user.profile

    if user_profile in post.liked_by.all():
        messages.warning(request, 'You have already liked this post.')
    else:
        post.liked_by.add(user_profile)
        post.likes += 1
        post.save()
        messages.success(request, 'Post liked successfully.')
    return redirect('post', pk=pk)

def dislikePost(request, pk):
    post = Post.objects.get(id=pk)
    user_profile = request.user.profile
    
    if user_profile not in post.liked_by.all():
        messages.warning(request, 'You have not liked this post yet.')
    else:
        post.liked_by.remove(user_profile)
        post.likes -= 1
        post.save()
        messages.success(request, 'Post disliked successfully.')
    return redirect('post', pk=pk)