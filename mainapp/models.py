from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=50, verbose_name='Название города', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return f"{self.pk}. {self.city_name}"

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('city_name', )    # Индексация по нужному полю # Сортировка по какому полю


class DataWeather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Город')
    date_time = models.DateTimeField(auto_now_add=False, verbose_name='дата')

    # time = models.CharField(max_length=10, verbose_name='Время')

    temperature = models.IntegerField(verbose_name='Температура')

    weather = models.CharField(max_length=50, verbose_name='Погода')
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return f" Погода в {self.city}"

    class Meta:
        verbose_name = 'Погода'
        verbose_name_plural = 'Погодные условия'
