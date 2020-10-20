from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ArchiveIndexView, YearArchiveView

from .forms import PostForm

# message 이용
from django.contrib import messages

@login_required
def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.save()
      messages.success(request, '포스팅을 저장했습니다.')
      return redirect(post)
  else:
    form = PostForm()
  return render(request, 'instagram/post_form.html', {
    'form': form,
    'post': None,
  })

@login_required
def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)

  if post.author != request.user:
    messages.error(request, '작성자만 작성할 수 있습니다.')
    return redirect(post)

  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save()
      messages.success(request, '포스팅을 수정했습니다.')
      return redirect(post)
  else:
    form = PostForm(instance=post)
  return render(request, 'instagram/post_form.html', {
    'form': form,
    'post': post,
  })

@login_required
def post_delete(request, pk):
  post = get_object_or_404(Post, pk=pk)

  if request.method == 'POST':
    post.delete()
    messages.success(request, '포스팅을 삭제했습니다.')
    return redirect('instagram:post_list')
  return render(request, 'instagram/post_confirm_delete.html', {
    'post': post,
  })

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

#   if q:
#     qs = qs.filter(message__icontains=q)

#   messages.info(request, 'messages 테스트')

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
    if not self.request.user.is_authenticated:
      qs = qs.filter(is_public=True)
    return qs

post_detail = PostDetailView.as_view()


post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)