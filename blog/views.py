from django.shortcuts import  get_object_or_404, redirect, render

from blog.models import Blog,Category
from django.db.models import Q 
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(status='Published',category=category_id)
    try:
        category=Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context) 

def blogs(request,slug):
    single_blog=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'single_blog':single_blog
    }
    return render(request,'blogs.html',context)

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blog.objects.filter(Q(title_icontains=keyword) | Q(short_description_icontians=keyword) |Q(blog_body_icontians=keyword),status='Published')
    context={
        'blogs':blogs,
        'keyword':keyword,
    }
    return render(request,'search.html',context) 
