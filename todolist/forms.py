from django import forms

class createNewListForm(forms.Form):
    name = forms.CharField(label="toDoList Name",max_length=200)