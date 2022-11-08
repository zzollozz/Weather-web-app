from mainapp.models import City, DataWeather

def get_citys():
    citys = City.objects.all()
    return citys

def get_dataweather_city():
    city_dataweather = DataWeather.objects.filter(is_active=True).select_related('city')
    return city_dataweather
