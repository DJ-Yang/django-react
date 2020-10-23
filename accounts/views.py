from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

# CBV
from django.views.generic import TemplateView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# 유저 모델
from django.contrib.auth import get_user_model, login as auth_login
from django.conf import settings

User = get_user_model()

# @login_required
# def profile(request):
#   return render(request, 'accounts/profile.html', {})

class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'accounts/profile.html'


profile = ProfileView.as_view()

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#   model = Profile
#   form_class = ProfileForm

# profile_edit = ProfileUpdateView.as_view()

@login_required
def profile_edit(request):
  try:
    profile = request.user.profile
  except Profile.DoesNotExist:
    profile = None

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      profile.save()
      return redirect('accounts:profile')
  else:
    form = ProfileForm(instance=profile)
  return render(request, 'accounts/profile_form.html', {
    'form': form,
  })

signup = CreateView.as_view(
  model=User,
  form_class=UserCreationForm,
  success_url=settings.LOGIN_URL,
  template_name='accounts/signup_form.html',
)

# def signup(request):
#   pass

def logout(request):
  pass