from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}), label='')
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Телефон'}), required=True, label='')


choices = (
        ('images/icons/1.png', mark_safe(_(
            '<img src="../static/images/icons/1.png" '
            'title="approve">',
            ))),
        ('images/icons/2.png', mark_safe(_(
            '<img src="../static/images/icons/2.png" '
            'title="approve">',
            ))),
        ('images/icons/3.png', mark_safe(_(
            '<img src="../static/images/icons/3.png" '
            'title="approve">',
            ))),
        ('images/icons/4.png', mark_safe(_(
            '<img src="../static/images/icons/4.png" '
            'title="approve">',
            ))),
        ('images/icons/5.png', mark_safe(_(
            '<img src="../static/images/icons/5.png" '
            'title="approve">',
            ))),
        ('images/icons/6.png', mark_safe(_(
            '<img src="../static/images/icons/6.png" '
            'title="approve">',
            ))),
        ('images/icons/7.png', mark_safe(_(
            '<img src="../static/images/icons/7.png" '
            'title="approve">',
            ))),
    )


class ReviewForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}), label='')
    surname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}), label='')
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Текст'}), label='')
    image = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, label='')
    # phone = forms.CharField(widget=forms.Input(attrs={'placeholder': 'Телефон'}), required=True, label='')
