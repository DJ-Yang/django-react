from django.urls import path, include, register_converter
from . import views

# Converter 커스텀
# class YearConverter:
#   regex = '\d{4}'
#   def to_python(self, value):
#     return int(value)
#   def to_url(self.value):
#     return str(value)

# register_converter(YearConverter, 'year')

# <int:pk> 여기에서 int에 해당하는 것이 converter


app_name='instagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail),
]
