from django.db import models
from posts.models import User_posts
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.
content_type = ContentType.objects.get_for_model(User_posts)
permission = Permission.objects.create(
    codename="can_publish",
    name="Can Publish Posts",
    content_type=content_type
)