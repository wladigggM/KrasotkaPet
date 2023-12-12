from django import forms
from .models import *


# class AddReview(forms.Form):
#     CHOICES = (('Option 1', '1'), ('Option 2', '2'), ('Option 3', '3'), ('Option 4', '4'), ('Option 5', '5'))
#     name = forms.CharField(max_length=255, label='Имя')
#     email = forms.CharField(max_length=255, label='Email')
#     rating = forms.ChoiceField(choices=CHOICES, label='Рейтинг')
#     comment = forms.CharField(widget=forms.Textarea(), label='Комментарий')

class AddReview(forms.ModelForm):
    class Meta:
        CHOICES = (('☆', '1'), ('☆☆', '2'), ('☆☆☆', '3'), ('☆☆☆☆', '4'), ('☆☆☆☆☆', '5'))
        model = Reviews
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=CHOICES),
            'comment': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }
        labels = {
            'name': 'Имя',
            'email': 'Email',
            'rating': 'Рейтинг',
            'comment': 'Комментарий'
        }