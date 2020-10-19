from django.conf import settings
from django.db import models
from django.urls import reverse

# 장고 폼 강의
from django.core.validators import MinLengthValidator

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
  message = models.TextField(
    validators=[MinLengthValidator(10)]
  )
  photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%M/%d')
  tag_set = models.ManyToManyField('Tag', blank=True)
  in_public = models.BooleanField(default=False, verbose_name='공개여부')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.message

  # 디테일 페이지로 이동할 수 있는 모델 메소드(강사 추천)
  def get_absolute_url(self):
    return reverse('instagram:post_detail', args=[self.pk])

  class Meta:
    ordering = ['-id']

class Tag(models.Model):
  name = models.CharField(max_length=100, unique=True)