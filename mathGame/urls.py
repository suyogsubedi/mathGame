from django.contrib import admin
from django.urls import path,include

"""
All the parents URL for the application
"""
urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')) ,
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('accounts/',include('allauth.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members/',include('members.urls'))
]
