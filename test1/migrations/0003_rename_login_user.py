# Generated by Django 4.2.4 on 2023-10-22 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_remove_login_date_login_email_login_mobile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='login',
            new_name='User',
        ),
    ]