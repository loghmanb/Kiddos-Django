# Generated by Django 3.1 on 2020-09-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_postcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Is published!'),
        ),
    ]
