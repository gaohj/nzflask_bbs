# Generated by Django 2.0 on 2020-02-28 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=30)),
                ('g_price', models.FloatField(default=1.0)),
            ],
        ),
    ]