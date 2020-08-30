# Generated by Django 3.1 on 2020-08-30 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200830_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('price', models.FloatField(verbose_name='Price')),
                ('duration', models.IntegerField(verbose_name='Duration')),
                ('short_desc', models.CharField(max_length=256, verbose_name='Short Description')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Image')),
                ('plan_cls', models.CharField(blank=True, max_length=20, null=True, verbose_name='Plan Style Class')),
            ],
            options={
                'db_table': 'kiddos_pricingplan',
            },
        ),
    ]
