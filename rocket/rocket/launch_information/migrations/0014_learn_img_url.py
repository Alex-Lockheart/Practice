# Generated by Django 2.2.5 on 2019-09-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launch_information', '0013_learn_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='learn',
            name='img_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
