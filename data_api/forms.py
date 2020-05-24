""" Data Forms for the Module - data_api """

import datetime

from django import forms
from django.core.exceptions import ValidationError

from data_api.models import Greeting


class GreetingForm(forms.ModelForm):
    """ A form creation of Greetings """

    class Meta:
        model = Greeting
        fields = '__all__'

    def clean_thedate(self) -> datetime.date:
        thedate = self.cleaned_data.get('thedate')
        if not isinstance(thedate, datetime.date):
            raise ValidationError('Invalid value in the "thedate" field')
        return thedate
