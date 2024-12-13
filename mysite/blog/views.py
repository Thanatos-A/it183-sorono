from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
from blog.models import Post
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

def blog_list(request):
    post = Post.objects.all()
    context = {
        'blog_list': post
    }
    return render(request, "blog/blog_list.html", context)

def blog_detail(request, id):
    each_post = Post.objects.get(id=id)
    context = {
        'blog_detail': each_post
    }
    return render(request, "blog/blog_detail.html", context)

def blog_delete(request, id):
    each_post = Post.objects.get(id=id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')

def blog_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():  # Ensure proper indentation here
        form.save()
        return HttpResponseRedirect('/posts/')
    context = {
        "form": form
    }
    return render(request, "blog/blog_create.html", context)

def blog_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts/')
    context = {
        "form": form,
        'form_type': 'Create',
    }
    return render(request, "blog/blog_create.html", context)

class ViewPosts(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class  = PostSerializer
