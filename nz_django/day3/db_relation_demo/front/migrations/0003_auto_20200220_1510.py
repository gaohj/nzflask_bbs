# Generated by Django 2.0 on 2020-02-20 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_userextension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extension', to='front.FrontUser'),
        ),
    ]
