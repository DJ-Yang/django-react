from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(requset: HttpRequest) -> HttpResponse:
  posts = Post.objects.all()

  return render(request, 'instagram/post_list.html', {
    'posts': posts,
  })

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#   post = get_object_or_404(Post, pk=pk)
#   # try:
#   #   post = Post.objects.get(pk=pk)
#   # except Post.DoesNotExist:
#   #   raise Http404
#   return render(request, 'instagram/post_detail.html', {
#     'post': post,
#   })

post_detail = DetailView.as_view(model=Post)