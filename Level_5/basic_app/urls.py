from django.urls import path, include, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^registration/$',views.registration, name='registration'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
]
