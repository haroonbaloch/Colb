from django import forms
from ColorBlind_App.models import Color


class NewUserForm(forms.ModelForm):
    class Meta():
        model=Color
        fields='__all__'
