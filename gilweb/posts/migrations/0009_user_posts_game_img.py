# Generated by Django 4.0.4 on 2022-06-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_user_posts_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_posts',
            name='game_img',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
