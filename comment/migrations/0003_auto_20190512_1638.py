# Generated by Django 2.0.13 on 2019-05-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20190512_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='page',
        ),
        migrations.AddField(
            model_name='comment',
            name='page_url',
            field=models.CharField(default='https://university.innopolis.ru/en/', max_length=500),
        ),
    ]
