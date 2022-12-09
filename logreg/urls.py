from django.urls import path,include
from django.views.generic.base import TemplateView
from.import views

urlpatterns = [
    path('',TemplateView.as_view(template_name='login.html'),name='admission/'),
    # path('', views.index),
    path('admission', views.login),
    path("admission/proctor_form",include("usersite.urls")),
    path('registration', views.registration, name='registration'),
    path('logout', views.logout_view, name='logout'),
    
]
