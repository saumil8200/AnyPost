from .models import Post, Category
from django.db.models import Q

def searchPosts(request):
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')

    categories = Category.objects.filter(name__icontains=search)    

    posts = Post.objects.distinct().filter(
        Q(title__icontains=search) | 
        Q(description__icontains=search) |
        Q(category__in=categories)
        )
    
    return posts, search

def searchCategories(request):
    search = ''

    if request.GET.get('search'):
        search = request.GET.get('search')

    categories = Category.objects.filter(name__icontains=search)

    return categories, search