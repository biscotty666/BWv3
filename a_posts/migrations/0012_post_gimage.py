# Generated by Django 5.0 on 2024-01-07 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0011_likedreply_reply_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gimage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]