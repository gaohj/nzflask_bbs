# Generated by Django 2.0 on 2020-02-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=30)),
                ('m_price', models.FloatField(default=1.0)),
            ],
        ),
    ]
