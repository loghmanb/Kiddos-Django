# Generated by Django 3.1 on 2020-08-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_pricingplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='Tags'),
        ),
    ]
