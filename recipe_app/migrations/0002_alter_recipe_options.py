# Generated by Django 5.0.1 on 2024-01-15 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name']},
        ),
    ]
