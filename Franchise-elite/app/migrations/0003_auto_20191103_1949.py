# Generated by Django 2.2.6 on 2019-11-04 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191103_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game_list',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Team'),
        ),
    ]
