# Generated by Django 4.0.4 on 2023-01-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0005_alter_pokemon_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_ar',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_fr',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name_jp',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
