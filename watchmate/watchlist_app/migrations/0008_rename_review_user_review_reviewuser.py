# Generated by Django 4.1.4 on 2023-01-18 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_review_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_user',
            new_name='reviewuser',
        ),
    ]
