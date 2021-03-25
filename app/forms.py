from django import forms

class BookAShowForm(forms.Form):
    your_name = forms.CharField(label ='Your name', max_length=100)