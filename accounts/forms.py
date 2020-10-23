from django import forms
from .models import Profile

# login quiz
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['address', 'zipcode']

class LoginForm(AuthenticationForm):
  # 퀴즈 입력 필드
  answer = forms.IntegerField(help_text = '3 + 3 = ?')

  # 퀴즈 확인 부분
  def clean_answer(self):
    answer = self.cleaned_data.get('answer')
    if answer != 6:
      raise forms.ValidationError('땡~!')
    return answer