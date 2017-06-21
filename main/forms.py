from django import forms

class AddBookForm(forms.Form):
    bookname=forms.CharField(max_length = 80)
    auth = forms.CharField(max_length=40)
    price = forms.IntegerField()