from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect

from mainapp.forms import CityForm, DataWeatherForm
from mainapp.models import DataWeather
from mainapp.services import get_citys, get_dataweather_city
from django.urls import reverse


def index(request):

    context = {
        'citys': get_citys(),
        # 'dataweather': dataweather
    }
    return render(request, 'mainapp/index.html', context)


def data_weather_in_city(request, pk):

    data_weather_in_city = DataWeather.objects.filter(city=pk)

    context = {
        'citys': get_citys(),
        'dataweather': data_weather_in_city
    }
    return render(request, 'mainapp/index.html', context)


def city_selection(request):

    context = {
        'city_selection': get_citys()
    }
    return render(request, 'mainapp/index.html', context)

# @login_required
def data_input(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
            city_name = CityForm(request.POST)
            data_weather = DataWeatherForm(request.POST)
            if city_name.is_valid() and data_weather.is_valid():
                city_name.save()
                data_weather.save()
                return redirect('index')

        city_name = CityForm()
        data_weather = DataWeatherForm()
        context = {
            'city_name': city_name,
            'data_weather': data_weather
        }
        return render(request, 'mainapp/data_input.html', context)
    else:
        return HttpResponseRedirect(reverse('mainapp:index'))

