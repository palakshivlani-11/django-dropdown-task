# Generated by Django 3.2.5 on 2021-10-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropdown', '0009_userresponses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponses',
            name='district',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
