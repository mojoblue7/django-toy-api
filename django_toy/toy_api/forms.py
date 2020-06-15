from django import forms

CHOICES = [
    ("남", "남성"),
    ("여", "여성")
]

class SignUpForm(forms.Form):
    email = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()
    gender = forms.ChoiceField(choices=CHOICES)
