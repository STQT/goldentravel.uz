# Generated by Django 3.2.14 on 2022-08-03 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20220801_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='short_desctions',
            field=models.CharField(default=1, max_length=200, verbose_name='Короткое описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tours',
            name='description',
            field=models.TextField(verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='tours', verbose_name='Основное изображение'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='tourshots',
            name='image',
            field=models.ImageField(upload_to='tourshots', verbose_name='Доп. изображение'),
        ),
        migrations.CreateModel(
            name='TourBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image', models.ImageField(upload_to='', verbose_name='Баннер')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tours', verbose_name='Баннер тура')),
            ],
        ),
    ]
