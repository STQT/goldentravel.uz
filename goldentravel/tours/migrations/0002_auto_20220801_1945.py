# Generated by Django 3.2.14 on 2022-08-01 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tours',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
        migrations.AlterModelOptions(
            name='tourshots',
            options={'verbose_name': 'Изображение тура', 'verbose_name_plural': 'Изображения туров'},
        ),
        migrations.AlterField(
            model_name='tours',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='tours'),
        ),
    ]