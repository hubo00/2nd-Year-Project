# Generated by Django 3.1.7 on 2021-04-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]
