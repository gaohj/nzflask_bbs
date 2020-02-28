# Generated by Django 2.0 on 2020-02-28 08:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(6, message='最长50最短6位')])),
                ('m_password', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(6, message='最长50最短6位')])),
            ],
        ),
    ]
