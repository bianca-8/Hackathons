# Generated by Django 4.2.6 on 2024-01-28 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymemento_app', '0007_alter_memento_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memento',
            name='img',
        ),
        migrations.AddField(
            model_name='memento',
            name='img1',
            field=models.ImageField(blank=True, default='', upload_to='static/mementos_files/images'),
        ),
        migrations.AddField(
            model_name='memento',
            name='img2',
            field=models.ImageField(blank=True, default='', upload_to='static/mementos_files/images'),
        ),
        migrations.AddField(
            model_name='memento',
            name='img3',
            field=models.ImageField(blank=True, default='', upload_to='static/mementos_files/images'),
        ),
    ]