# Generated by Django 2.1.5 on 2019-02-16 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190216_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='user_id',
            new_name='username',
        ),
    ]
