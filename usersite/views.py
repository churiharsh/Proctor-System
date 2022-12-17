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
from .forms import admissionForm,personalDetailsForm,extraDetailsForm
from . models import admission_details,personal_details,current_semester
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



# def admission_details(request):
#   if(request.method =='POST'):
#        yearAdmission=int(request.POST['year_admission'])
#        categoryAdmission=request.POST['category_admission']
#        hscMarks=request.POST['hsc_marks']
#        cetMarks=request.POST['cet_marks']
#        jeeMarks=request.POST['jee_marks']
#        diplomaMarks=request.POST['diploma_marks']
#        userName=request.user
#        user=User.objects.get(username=userName)
#        print(user)
#        adm=admission_details(year_admission='2018',category_admission='TFWS',hsc_marks='56.5',cet_marks='45.3',jee_marks='34.6',diploma_marks='56.4',user=user)
#        adm.save()
#        return redirect('personalinfo.html')
#   else:
#        return render(request,'admission.html') 

#   return render(request,'admission.html')



def adm_details(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
           adm_details=admission_details.objects.filter(user=request.user).first()
           sem_details=current_semester.objects.filter(user=request.user).first()
        #    adm_details=admission_details.objects.get(user=request.user)
          #  print(adm_details.year_admission)
           form = admissionForm(request.POST,instance=adm_details)
           form2 = extraDetailsForm(request.POST,instance=sem_details)
           for field in form:
               print(field.value())

           if form.is_valid() and form2.is_valid():
            obj=form.save(commit=False)
            obj2=form2.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj2.user = User.objects.get(pk=request.user.id)
            obj.save()
            obj2.save()
            return redirect('personal_details/')
  
    else:
        adm_details=admission_details.objects.filter(user=request.user).first()
        sem_details=current_semester.objects.filter(user=request.user).first()
        if not adm_details:
              form = admissionForm()
              form2 = extraDetailsForm()

        # adm_details=admission_details.objects.filter(user=request.user.id)
        else:
          form = admissionForm(instance=adm_details)
          form2 = extraDetailsForm(instance=sem_details)

          print("Hello else")
          return render(request,'admission.html',{'form':form,'form2':form2})


    print("Hello")
    return render(request,'admission.html',{'form':form,'form2':form2})


def stud_personal_details(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
           psnl_details=personal_details.objects.filter(user=request.user).first()
           family_details_form=family_info.objects.filter(user=request.user).first()


        #    psnl_details=personal_details.objects.get(user=request.user)
        #    print(adm_details.year_admission)
           form = personalDetailsForm(request.POST,request.FILES,instance=psnl_details)
           familyForm = familyFatherDetailsForm(request.POST,request.FILES,instance=family_details_form)
        #    motherForm = familyMotherDetailsForm(request.POST,request.FILES,instance=mother_details_form)
           for field in form:
               print(field.value())

           if form.is_valid():
            obj=form.save(commit=False)
            obj2=familyForm.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj2.user = User.objects.get(pk=request.user.id)
            obj.save()
            ob2.save()
            return redirect('academic_details/')
  
    else:
        psnl_details = personal_details.objects.filter(user=request.user).first()
        family_details_form=family_info.objects.filter(user=request.user).first()

        
        # father_details_form = family_info_father.objects.filter(user=request.user).first()
        # mother_details_form = family_info_mother.objects.filter(user=request.user).first()
        if not psnl_details and family_details_form :
            form = personalDetailsForm()
            form2 = familyDetailsForm()
            # motherForm = familyMotherDetailsForm()
        else:
            form = personalDetailsForm(instance=psnl_details)    
            form2 = familyDetailsForm(instance=family_details_form)

           
            print("Hello else")
            return render(request,'personalinfo.html',{'form':form,'form2':form2})

    # form = personalDetailsForm()
    print("Hello")
    return render(request,'personalinfo.html',{'form':form,'form2':form2})


          


      

def academicDetails(request):
    return render(request,'academic.html')


# def fam_details(request):
#     if request.method == 'POST':
#         if request.user.is_authenticated:
#            father_details_form=family_info_father.objects.filter(user=request.user).first()
#         #    psnl_details=personal_details.objects.get(user=request.user)
#         #    print(adm_details.year_admission)
#            fatherForm = familyFatherDetailsForm(request.POST,request.FILES,instance=father_details_form)
#            for field in form:
#                print(field.value())

#            if form.is_valid():
#             obj=form.save(commit=False)
#             obj.user = User.objects.get(pk=request.user.id)
#             obj.save()
#             return redirect('academic_details/')
  
#     else:
#         father_details_form = familyFatherDetailsForm.objects.filter(user=request.user).first()
#         # print(admission_details.objects.filter(user=request.user.id))
#         if not psnl_details:
#             fatherForm = familyFatherDetailsForm()
#         else:
#             form = familyFatherDetailsForm(instance=father_details_form)    
#             print("Hello else")
#             return render(request,'personalinfo.html',{'form':form})

#     print("Hello")








  
   


