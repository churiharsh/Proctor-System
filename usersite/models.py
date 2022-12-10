from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime



class personal_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    # first_name=models.ForeignKey(first_name,max_length=50,on_delete=models.CASCADE)
    # last_name=models.ForeignKey(last_name,max_length=50,on_delete=models.CASCADE)
    middle_name=models.CharField(max_length=30)
    birth_place=models.CharField(max_length=30)
    mother_tongue=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=30)
    guardian_name=models.CharField(max_length=30),
    religion=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=30)
    stud_image=models.ImageField()
    stud_sign_image=models.ImageField()
    family_income=models.IntegerField()




class current_semester(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)    
    user =models.ForeignKey(User,on_delete=models.CASCADE)    
    current_sem=models.IntegerField()
    current_sem_num=models.IntegerField()



class semester_sub_ia(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    current_semester=models.ForeignKey('current_semester',on_delete=models.CASCADE)
    sub_1=models.CharField(max_length=30)
    sub_2=models.CharField(max_length=30)
    sub_3=models.CharField(max_length=30)
    sub_4=models.CharField(max_length=30)
    sub_5=models.CharField(max_length=30)
    sub_6=models.CharField(max_length=30)


class attendance(models.Model):
    current_sem=models.ForeignKey('current_semester',on_delete=models.CASCADE)
    # email=models.ForeignKey(user,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    default_list_num=models.IntegerField()
    is_defaulter=models.BooleanField()



    # family models

class family_relation(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      relation_type=models.CharField(max_length=30)



class family_info(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    femail=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    contact_num=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    occupation=models.CharField(max_length=30)
    relation_type=models.ForeignKey('family_relation',on_delete=models.CASCADE)



class admission_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    jee_marks=models.DecimalField(decimal_places=2,max_digits=5)
    hsc_marks=models.DecimalField(decimal_places=2,max_digits=5)
    cet_marks=models.DecimalField(decimal_places=2,max_digits=5)
    diploma_marks=models.DecimalField(decimal_places=2,max_digits=5)
    year_admission=models.IntegerField()
    category_admission=models.CharField(max_length=50)


    



