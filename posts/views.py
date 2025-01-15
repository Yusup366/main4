from django.shortcuts import render , HttpResponse
import random
from posts.models import Post


def main_view(request):
    return render(request,'main.html')


def posts_list_view(request):
    posts = Post.objects.all()
    return render(request,'posts_list.html',context = {'posts':posts})

def posts_detail_view(request,posts_id):
    posts = Post.objects.get(id=posts_id)
    return render(request,'posts_detail.html',context = {'posts':posts})



