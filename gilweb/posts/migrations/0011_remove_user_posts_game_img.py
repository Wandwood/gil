# Generated by Django 4.0.4 on 2022-06-21 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_user_posts_game_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_posts',
            name='game_img',
        ),
    ]