# Generated by Django 2.2.12 on 2022-07-18 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220718_1100'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutUser',
            new_name='UserInfo',
        ),
    ]
