# Generated by Django 3.2.14 on 2022-08-03 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_alter_tours_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourshots',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shots', to='tours.tours'),
        ),
    ]