# Generated by Django 4.2.6 on 2024-01-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymemento_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memento',
            name='audio',
            field=models.FileField(default='', upload_to='static/mementos_files/audios'),
        ),
        migrations.AlterField(
            model_name='memento',
            name='img',
            field=models.ImageField(default='', upload_to='static/mementos_files/images'),
        ),
    ]