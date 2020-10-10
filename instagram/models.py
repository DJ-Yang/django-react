from django.conf import settings
from django.db import models


class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
  message = models.TextField()
  photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%M/%d')
  tag_set = models.ManyToManyField('Tag', blank=True)
  in_public = models.BooleanField(default=False, verbose_name='공개여부')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.message

  class Meta:
    ordering = ['-id']

class Tag(models.Model):
  name = models.CharField(max_length=100, unique=True)