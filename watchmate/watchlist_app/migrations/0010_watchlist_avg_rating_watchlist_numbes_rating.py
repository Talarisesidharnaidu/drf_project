# Generated by Django 4.1.4 on 2023-02-06 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0009_rename_reviewuser_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='numbes_rating',
            field=models.IntegerField(default=0),
        ),
    ]
