# Generated by Django 3.1.7 on 2021-05-17 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_backend', '0002_auto_20210517_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]