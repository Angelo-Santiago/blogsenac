# blog/forms.py
from django import forms
from .models import Publication

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['author', 'pub_title', 'pub_text']
