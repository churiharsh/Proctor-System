from django import forms

class admissionForm(forms.Form):
    year=forms.IntegerField()
    category=forms.CharField(max_length=50)
    hsc_score=forms.DecimalField(max_digits=4)
    cet_score=forms.DecimalField(max_digits=4)
    jee_score=forms.DecimalField(max_digits=4)
    diploma_score=forms.DecimalField(max_digits=4)

