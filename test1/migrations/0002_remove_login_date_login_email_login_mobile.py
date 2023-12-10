# Generated by Django 4.2.4 on 2023-10-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='date',
        ),
        migrations.AddField(
            model_name='login',
            name='email',
            field=models.EmailField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='login',
            name='mobile',
            field=models.IntegerField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]