from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from usersite.views import submit_personalinfo
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    # path('',views.home_view),
    path('',views.adm_details),
    path('page1/',views.stud_personal_details),
    path('page2/',views.academicDetails),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)