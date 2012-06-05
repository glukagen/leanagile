from django import forms


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    photo = forms.FileField(required=False)
    specialities = forms.CharField(widget=forms.Textarea())
    about_me = forms.CharField(widget=forms.Textarea(), required=False)
