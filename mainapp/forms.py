from django import forms
from django.forms import TextInput, NumberInput
from django.forms.widgets import DateTimeBaseInput

from mainapp.models import City, DataWeather


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city_name']
        widgets = {
            'city_name': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Город"
            })
        }


class DataWeatherForm(forms.ModelForm):
    class Meta:
        model = DataWeather
        fields = ['date_time', 'temperature', 'weather']
        # exclude =()
        widgets = {
            'date_tim': DateTimeBaseInput(attrs={
                "class": "form-control",
                "placeholder": "Дата"
            }),
            'temperature': NumberInput(attrs={
                "class": "form-control",
                "placeholder": "температура"
            }),
            'weather': TextInput(attrs={
                "class": "form-control",
                "placeholder": "условия погоды"
            })
        }


