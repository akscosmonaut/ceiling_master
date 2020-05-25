from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}), label='')
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Телефон'}), required=True, label='')


class ReviewForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}), label='')
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}), label='')
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Текст'}), label='')
    # phone = forms.CharField(widget=forms.Input(attrs={'placeholder': 'Телефон'}), required=True, label='')