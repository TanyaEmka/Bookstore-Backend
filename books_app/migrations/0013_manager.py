# Generated by Django 3.2.15 on 2022-12-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0012_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('publisher_id', models.IntegerField()),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
    ]
