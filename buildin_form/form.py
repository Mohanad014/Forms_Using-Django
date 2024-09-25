from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    age = forms.IntegerField(label='age')
    email = forms.EmailField(label='email')
    address = forms.CharField(label='address', widget=forms.Textarea)
    