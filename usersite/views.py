from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import admissionForm





def index(request):
  return redirect('admission.html')

    



def home_view(request):
  context={}
  context['form']=admissionForm()
  return render(request,"admission.html",context)



def get_details(request):
  if not request.user.is_authenticated:
    return redirect('unauthorised')
  else:
     if request.method == 'POST':
      hsc = request.POST['hsc_marks']
      # cet = request.POST.get('cet')
      # jee = request.POST.get('jee')
      # diploma = request.POST.get('diploma')
      # print(year,category,hsc,cet,jee)
      # da = admission(year=year,category=category,hsc=hsc,cet=cet,jee=jee,diploma=diploma)
      # da.save()

     return render(request,'admission.html')


  






# @login_required
def submit_admission(request):
  
    if request.user.is_authenticated:

      user = request.user
      print(user)
      form = admissionForm(request.POST)
      if form.is_valid():
        print(form.cleaned_data)
        admission = form.save(commit=False)
        admission.user = user
        admission.save()


        return redirect("personalinfo")
      else:
        return render(request,'admission.html',context = {'form': form})



""" @login_required
def personalinfo(request):
 if not request.user.is_authenticated:
    return redirect('unauthorised')
 else:
    user = request.user
    print(user)
    form = personalinfoForm()
    try:
      personalinfo1 = personalinfo2.objects.filter(user=user).latest('pk')
    except:
      personalinfo1 = personalinfo2.objects.filter(user=user)

    return render(request,'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1}) """


""" @login_required   BY rishabh
def personalinfo(request):

  if  request.user.is_authenticated:

      user = request.user
      print(user)
      form = personalinfoForm()
      this_user = User.objects.get(username=user)
      print(this_user)
      personalinfo1 = personalinfo2.objects.filter(user=this_user)
      print(personalinfo1)
      return render(request,'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})
      # return render(request,'personalinfo.html', context={'form': form})

  else:
      return redirect('unauthorised')



@login_required
def submit_personalinfo(request):
      try:
        if request.user.is_authenticated:

          user = request.user
          # print(user)
          # print(user)
          form = personalinfoForm(request.POST)
          try:
            if request.method == 'POST':
              print(5)
              # print(user)
              print(form.cleaned_data)
              personalinfo = form.save(commit=False)
              personalinfo.user = user
              personalinfo.save()
              print(1)
              return redirect('academic')

          except:
            print(4)
            if form.errors:
              for error in form.errors:
                print("Error:  ",error)

            return redirect('academic')

          else:
            print(2)
            return redirect('personalinfo')

      except Exception:
        print(Exception)
        print(3) """



@login_required
def personalinfo(request):
  if  request.user.is_authenticated:

      user = request.user
      print(user)
      form = personalinfoForm()
      try:
        print(1)
        personalinfo1 = personalinfo2.objects.filter(user=user).latest('pk')
      except:
        print(2)
        personalinfo1 = personalinfo2.objects.filter(user=user)
      return render(request,'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})

  else:
      return redirect('unauthorised')


def submit_personalinfo(request):

    if request.user.is_authenticated:

      user = request.user
      print("submit",user)
      form = personalinfoForm(request.POST)
      print("after form",user)
      if form.is_valid():
        print('Form Valid')
        print(form.cleaned_data)
        personalinfo = form.save(commit=False)
        personalinfo.user = user
        personalinfo.save()


        return redirect("academic")
      else:
        
        print("Form skipped")
        return render(request,'personalinfo.html',context = {'form': form})




















@login_required
def academic(request):
  if  request.user.is_authenticated:

      user = request.user
      print(user)
      form = academicForm()
      try:
        academic1 = academic2.objects.filter(user=user).latest('pk')
      except:
        academic1 = academic2.objects.filter(user=user)
      return render(request,'academic.html', context={'form': form, 'academic1': academic1})

  else:
      return redirect('unauthorised')


def submit_academic(request):

    if request.user.is_authenticated:

      user = request.user
      print(user)
      form = academicForm(request.POST)
      if form.is_valid():
        print(form.cleaned_data)
        academic = form.save(commit=False)
        academic.user = user
        academic.save()


        return redirect("achievementdetails")
      else:
        return render(request,'academic.html',context = {'form': form})




@login_required
def achievementdetails(request):
  if not request.user.is_authenticated:
    return redirect('unauthorised')
  else:
    return render(request,'achievements.html')

""" @login_required
def personalinfo(request):
 if not request.user.is_authenticated:
    return redirect('unauthorised')
 else:
    return render(request,'personalinfo.html') """

@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

def unauthorised(request):
    return render(request,'unauthorised.html')



