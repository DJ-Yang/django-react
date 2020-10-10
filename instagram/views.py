from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


# 리스트 뷰 이용 방법
# 방법 1
# post_list = ListView.as_view(model=Post, paginate_by=10)
# 방법 2
# @method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
  model = Post
  # 페이지네이션 기능 제공
  paginate_by = 10

  def get_queryset(self):
    qs = super().get_queryset()
    qs = qs.filter()
    return qs

post_list = PostListView.as_view()

# @login_required
# def post_list(request: HttpRequest) -> HttpResponse:

#   q = request.GET.get("q", '')
#   qs = Post.objects.all()
#   print(q)
#   if q:
#     qs = qs.filter(message__icontains=q)

#   print(q)
#   return render(request, 'instagram/post_list.html', {
#     'post_list': qs,
#     'q': q,
#   })

# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#   post = get_object_or_404(Post, pk=pk)
#   # try:
#   #   post = Post.objects.get(pk=pk)
#   # except Post.DoesNotExist:
#   #   raise Http404
#   return render(request, 'instagram/post_detail.html', {
#     'post': post,
#   })


#  디테일 뷰를 이용하는 두 가지 방법
# 방법 1
# post_detail = DetailView.as_view(model=Post)

# 방법 2
class PostDetailView(DetailView):
  model = Post
  # queryset = Post.objects.filter(is_public=True)

  # 조건 나누기 (reqeust 인자는 self.request에 있다.)
  def get_queryset(self):
    qs = super().get_queryset()
    # 로그인이 안되어있다면 is_public이 True인 파일만 확인
    if not self.request.user.is_authenticiated:
      qs = qs.filter(is_public=True)
    return qs

post_detail = PostDetailView.as_view()