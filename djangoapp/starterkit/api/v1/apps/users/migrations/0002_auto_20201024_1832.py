# Generated by Django 3.0.7 on 2020-10-24 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='favorite_placess',
            new_name='favorite_places',
        ),
    ]
