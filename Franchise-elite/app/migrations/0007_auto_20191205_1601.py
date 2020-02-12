# Generated by Django 2.2.6 on 2019-12-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191112_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='photo',
            field=models.ImageField(default='noImageAttached.png', upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='log',
            name='fldGoalAtt',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='log',
            name='fldGoalMade',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_id',
            field=models.IntegerField(),
        ),
    ]