from django import forms
from .models import home
from django.core import validators
from django.forms import widgets


class homeform(forms.ModelForm):
        name = forms.CharField(validators=[validators.EmailValidator])
        start_date=forms.DateTimeField()
        end_date= forms.DateTimeField()
        def clean(self):
            cleanned_date=super().clean()
            start=cleanned_date.get('start_date')
            end=cleanned_date.get('end_date')
            if str(end) < str(start):
                raise forms.ValidationError('enter qwertyuyt')

        class Meta:
            model = home
            fields={'name','number','email','start_date','end_date'}

        # widgets={
        #     "start_date":forms.DateInput(attrs={'class':"form-control",'placeholder':'Enter date'})
        # }