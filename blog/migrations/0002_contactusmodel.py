# Generated by Django 2.2.12 on 2022-06-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
