from django import forms
from persons.models import Person, ToDo


class AdminSettingsForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['email', 'first_name', 'last_name', 'tg_id']
        labels = {
            'email': 'Почта',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'tg_id': 'Телеграм ID',
        }
