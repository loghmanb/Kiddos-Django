# Generated by Django 3.1 on 2020-08-30 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/%Y/%m/%d/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
