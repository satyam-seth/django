from django import forms
from myapp.models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        exclude = ['title']
