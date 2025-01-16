from django.shortcuts import render , HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostCreateForm


def main_view(request):
    if request.method == 'GET':
        return render(request,'main.html')


def posts_list_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request,'posts_list.html',context = {'posts':posts})

def posts_detail_view(request,post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request,'posts_detail.html',context = {'post':post})


def posts_create_view(request):
    if request.method == 'GET':
        form = PostCreateForm()
        return render(request,'posts_create.html', context = {'form':form})
    if request.method == 'POST':
        form = PostCreateForm(request.POST,request.FILES)
        if not form.is_valid():
            return render(request,'posts_create.html',context = {'form':form})
        elif form.is_valid():
            form.save()
            return redirect('/posts/')

