# Generated by Django 3.1 on 2020-08-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_blogpost_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Is published!'),
        ),
    ]
