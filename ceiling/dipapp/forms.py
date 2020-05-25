from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}), label='')
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Телефон'}), required=True, label='')