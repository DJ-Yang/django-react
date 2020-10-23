from django.urls import path, include
from django.contrib.auth.views import LoginView

app_name='accounts'

urlpatterns = [
  # path('login', LoginView.as_view(), name='login'),
  path('login', LoginView.as_view(template_name='accounts/login_form.html'), name='login'), #템플릿 네임 지정
]