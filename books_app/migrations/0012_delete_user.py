# Generated by Django 3.2.15 on 2022-12-02 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0011_alter_user_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]