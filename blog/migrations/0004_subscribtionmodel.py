# Generated by Django 2.2.12 on 2022-06-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_subscribtionmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscribtionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs_email', models.CharField(max_length=100)),
            ],
        ),
    ]