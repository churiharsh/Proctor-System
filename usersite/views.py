from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
# from .forms import admissionForm
from . models import admission_details
from django.contrib import messages
from django.contrib.auth import get_user_model
from logreg.views import registration


User=get_user_model()

# def index(request):
#   return redirect('admission')

    



def home_view(request):
  # context={}
  # context['form']=admissionForm()
  return render(request,"admission.html")



def admission_details(request):
  if(request.method =='POST'):
       yearAdmission=request.POST['year_admission']
       categoryAdmission=request.POST['category_admission']
       hscMarks=request.POST['hsc_marks']
       cetMarks=request.POST['cet_marks']
       jeeMarks=request.POST['jee_marks']
       diplomaMarks=request.POST['diploma_marks']
       userName=request.session.get(registration.username)
      #  user=User.objects.get(username=userName)
       print(userName)
      #  adm=admission_details(year_admission=yearAdmission,category_admission=categoryAdmission,hsc_marks=hscMarks,cet_marks=cetMarks,jee_marks=jeeMarks,diploma_marks=diplomaMarks,user=user)
      #  adm.save()
       return redirect('personalinfo.html')
  else:
       return render(request,'admission.html') 

  return render(request,'admission.html')



# def admission_details(request):
#     if request.method == 'POST':
#         user_name=request.session.get('username')
#         user = User.objects.get(username='bbutcher')
#         form = admissionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('personalinfo.html')
  
#     else:
#         form = admissionForm()
#         context = {
#             'form':form,
#         } 
#         return render(request,'admission.html',{'form':form})

#     return render(request, 'admission.html', {'form':form})

          


      

  







  
   


