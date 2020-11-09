from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField(initial='Sonam',help_text='isme 30 character hi likh sakte hai.')