# Generated by Django 4.0.4 on 2022-06-14 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_user_posts_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_posts',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
