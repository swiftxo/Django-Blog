# Generated by Django 5.0.4 on 2024-05-02 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0011_rename_userprofile_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
