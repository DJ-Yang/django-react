from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import LoginForm

app_name='accounts'

urlpatterns = [
  # path('login', LoginView.as_view(), name='login'),
  path('logout', LogoutView.as_view(), name='logout'),
  # path('logout/', views.logout, name='logout'),
  path('login/', LoginView.as_view(
    form_class=LoginForm,
    template_name='accounts/login_form.html'
    ), name='login'), #템플릿 네임 지정
  path('profile/', views.profile, name='profile'),
  path('profile/edit/', views.profile_edit, name='profile_edit'),
  path('signup/', views.signup, name='signup'),
]