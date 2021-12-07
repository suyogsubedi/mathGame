
from django.urls import path
from . import views

"""
List of URL related to logging user in and out
"""
urlpatterns = [
    path('login_user', views.login_user,name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user')

]
