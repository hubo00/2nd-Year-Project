# Generated by Django 3.1.7 on 2021-02-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210221_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name_alt',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
