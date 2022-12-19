from django.db import models
from django.contrib.auth.models import User



class personal_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    middle_name=models.CharField(max_length=30)
    birth_place=models.CharField(max_length=30)
    birth_date=models.DateField()
    mother_tongue=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=30)
    guardian_name=models.CharField(max_length=30,default="NULL")
    religion=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=30)
    disease=models.CharField(max_length=30,default="None")
    address=models.CharField(max_length=100,default="NULL")
    stud_image=models.ImageField(upload_to ="images/")
    stud_sign_image=models.ImageField(upload_to ="images/")
    email=models.CharField(max_length=30,default="NULL")
    family_income=models.IntegerField(default=10000)




class current_semester(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)    
    user =models.ForeignKey(User,on_delete=models.CASCADE)    
    CURRENT_YEAR_CHOICES =[
        ('FE','FE'),
        ('SE','SE'),
        ('TE','TE'),
        ('BE','BE'),
        
    ]
    current_year=models.CharField(max_length=50,choices=CURRENT_YEAR_CHOICES)
    CURRENT_SEM_CHOICES =[
        ('SEM 1','SEM 1'),
        ('SEM 2','SEM 2'),
        ('SEM 3','SEM 3'),
        ('SEM 4','SEM 4'),
        ('SEM 5','SEM 5'),
        ('SEM 6','SEM 6'),
        ('SEM 7','SEM 7'),
        ('SEM 8','SEM 8'),
    ]
    BRANCH_CHOICES =[
        ('INFT','INFT'),
        ('MECHANICAL','MECHANICAL'),
        ('AI & DS','AI & DS'),
        ('CIVIL','CIVIL'),
        ('CS','CS'),
        ('EXTC','EXTC'),
    ]
    branch = models.CharField(max_length=50,choices =BRANCH_CHOICES,default='INFT')
    current_sem=models.CharField(max_length=50,choices=CURRENT_SEM_CHOICES)


class roll_no(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     roll_no = models.IntegerField()
    
     sem=models.CharField(max_length=30)




   


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

# class family_relation(models.Model):
#     # email=models.ForeignKey(User,on_delete=models.CASCADE)
#       user=models.ForeignKey(User,on_delete=models.CASCADE)
#       PARENT_CHOICES = (
#         ('MOTHER','MOTHER'),
#         ('MOTHER','FATHER')
#       )
#       relation_type=models.CharField(max_length=30,choices=PARENT_CHOICES)



class family_info_father(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    fage=models.IntegerField()
    faddress=models.CharField(max_length=50)
    fcontact_num=models.CharField(max_length=30)
    femail=models.EmailField(max_length=50,default='xyz@gmail.com')
    fqualification=models.CharField(max_length=30)
    foccupation=models.CharField(max_length=30)
    father_image =models.ImageField()
    father_sign =models.ImageField()
    PARENT_CHOICES = (
         ('MOTHER','MOTHER'),
        ('MOTHER','FATHER')
    )
    # prelation=models.CharField(max_length=30,choices =PARENT_CHOICES)

class family_info_mother(models.Model):
    # email=models.ForeignKey(User,on_delete=models.CASCADE)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    mname=models.CharField(max_length=50)
    mage=models.IntegerField()
    maddress=models.CharField(max_length=50)
    mcontact_num=models.CharField(max_length=30)
    memail=models.EmailField(max_length=50,default='xyz@gmail.com')
    mqualification=models.CharField(max_length=30)
    moccupation=models.CharField(max_length=30)
    mother_image =models.ImageField()
    mother_sign =models.ImageField()



class admission_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    jee_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    hsc_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    cet_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    diploma_marks=models.DecimalField(max_length=50,max_digits=5,decimal_places=2)
    year_admission=models.IntegerField(default=0000)
    category_admission=models.CharField(max_length=50)


class sibling_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    sib_name=models.CharField(max_length=50,default='NULL')
    GENDER_CHOICES = (
        ('MALE','MALE'),
        ('FEMALE','FEMALE')
        )
    sib_gender = models.CharField(max_length=50,choices=GENDER_CHOICES)
    sib_age=models.CharField(max_length=50)
    sib_contact_num=models.CharField(max_length=30)
    sib_qualification=models.CharField(max_length=30)
    sib_occupation=models.CharField(max_length=30)



    


    



