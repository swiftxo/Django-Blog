# Generated by Django 5.0.4 on 2024-05-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0013_profile_soundcloud_link_profile_spotify_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
