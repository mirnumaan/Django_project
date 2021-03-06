# Generated by Django 3.2 on 2021-04-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_alter_slider_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('fb_id', models.CharField(max_length=255)),
                ('insta_id', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='media/team/%Y/')),
            ],
        ),
    ]
