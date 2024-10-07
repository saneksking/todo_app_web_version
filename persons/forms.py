from django import forms
from persons.models import Person


class SignUpForm(forms.ModelForm):
    password = forms.CharField(max_length=255)
    password_2 = forms.CharField(max_length=255)

    class Meta:
        model = Person
        fields = ['email', 'first_name', 'last_name', 'tg_id']

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            raise forms.ValidationError('Passwords dont\' match!')
        return cd['password_2']