""" Data models for the data_api module """

from django.db import models


class Greeting(models.Model):
    """ A Greeting Model """

    class Meta:
        verbose_name = 'Поздравление'
        verbose_name_plural = 'Поздравления'

    id = models.IntegerField(primary_key=True, verbose_name='id')
    category = models.CharField(max_length=50, null=False, blank=False, verbose_name='Категория')
    from_row = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Автор поздравления'
    )
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    text = models.TextField(null=False, blank=False, verbose_name='Текст')
    thedate = models.DateField(null=False, blank=False, verbose_name='Дата')

    def __str__(self) -> str:
        return str(f'Поздравление {self.id} от {self.from_row}, дата: {self.thedate}')
