from django import forms

class StudentRegistration(forms.Form):
    # name=forms.CharField()
    # name=forms.CharField(label='Your Name')
    # name=forms.CharField(label='Your Name',label_suffix=' ')
    # name=forms.CharField(label='Your Name',label_suffix=' ',initial='Sonam')
    # name=forms.CharField(label='Your Name',label_suffix=' ',initial='Sonam',required=False)
    # name=forms.CharField(label='Your Name',label_suffix=' ',initial='Sonam',required=False,disabled=True)
    name=forms.CharField(label='Your Name',label_suffix=' ',initial='Sonam',required=False,disabled=True,help_text='Limit 70 Char')
   