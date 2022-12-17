from django import forms
from django.forms import ModelForm
from . models import admission_details,personal_details,current_semester
from django.contrib.auth.models import User

class admissionForm(ModelForm):
     class Meta:
        model = admission_details
        fields = ['year_admission','category_admission','hsc_marks','cet_marks','jee_marks','diploma_marks']


class personalDetailsForm(ModelForm):
        class Meta:
                model = personal_details
                widgets ={
                        'birth_date':forms.TextInput(attrs={'placeholder':'YYYY/MM/DD'})
                 }
                fields = ['birth_place','mother_tongue','religion','address','phone_number','email','blood_group','guardian_name','birth_date','stud_sign_image','disease']



# class familyFatherDetailsForm(ModelForm):
#         class Meta:
#                 model = family_info_father
#                 fields=['fname','fage','faddress','fcontact_num','femail','fqualification','foccupation','fparent_image','fparent_sign'

#                 ]


class extraDetailsForm(ModelForm):
    class Meta:
        model = current_semester
        fields = ['current_year','current_sem']                 
# class familyMotherDetailsForm(ModelForm):
#         class Meta:
#                 model = family_info_mother
#                 fields=['mname','mage','maddress','mcontact_num','memail','mqualification','moccupation','mparent_image','mparent_sign',''

#                 ]



