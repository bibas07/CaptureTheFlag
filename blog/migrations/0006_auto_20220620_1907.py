# Generated by Django 2.2.12 on 2022-06-20 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220620_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactusmodel',
            old_name='email',
            new_name='cont_email',
        ),
    ]
