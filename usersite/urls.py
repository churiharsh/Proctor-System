from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from usersite.views import submit_personalinfo

urlpatterns = [

    #  path('',views.index),
    path('',views.home_view),
]