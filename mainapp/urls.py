from django.urls import path
from mainapp.views import index, data_input, data_weather_in_city, city_selection


urlpatterns = [
    path('', index, name='index'),
    path('data_input/', data_input, name='data_input'),
    path('select_city/<int:pk>/', data_weather_in_city, name='select_city'),
    path('city/', city_selection, name='city_selection'),
]
