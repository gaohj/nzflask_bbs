# Generated by Django 2.0 on 2020-02-19 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id']},
        ),
    ]
