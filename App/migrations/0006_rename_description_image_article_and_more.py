# Generated by Django 4.1.7 on 2023-04-03 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_image_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='description',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='message',
            new_name='topic',
        ),
    ]
