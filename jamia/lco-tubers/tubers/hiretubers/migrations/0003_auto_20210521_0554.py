# Generated by Django 3.1.4 on 2021-05-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0002_auto_20210520_1535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hiretuber',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='hiretuber',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
