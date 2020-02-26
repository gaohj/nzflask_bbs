# Generated by Django 2.0 on 2020-02-26 03:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(6)])),
                ('password', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(6)])),
                ('telephone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('1[3-9]\\d{9}', message='请输入正确的手机号')])),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
