# Generated by Django 3.2.5 on 2021-10-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropdown', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResponses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
    ]