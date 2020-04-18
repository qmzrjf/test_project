from django.forms import ModelForm
from django import forms
from profile_app.models import Customer


class DateInput(forms.DateInput):
    input_type = 'date'


class SignUpForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    date_of_birth = forms.DateField(widget=DateInput)

    class Meta:
        model = Customer
        fields = ('email', 'username', 'password', 'password2', 'date_of_birth')

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data['password'] != cleaned_data['password2']:
                raise forms.ValidationError('Password do not match! ')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
