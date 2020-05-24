# Generated by Django 3.0.6 on 2020-05-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
                ('from_row', models.CharField(max_length=50, verbose_name='Автор поздравления')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('thedate', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Поздравление',
                'verbose_name_plural': 'Поздравления',
            },
        ),
    ]