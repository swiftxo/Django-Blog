# Generated by Django 5.0.4 on 2024-05-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0012_profile_github_link_profile_instagram_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='soundcloud_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='spotify_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
