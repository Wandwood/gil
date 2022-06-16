from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class User_posts(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    post_header = models.CharField(max_length=200)
    game_name = models.CharField(max_length=150)
    post_text = models.CharField(max_length=5000)
    game_rating = models.DecimalField(max_digits=4, decimal_places=2)
    post_date = models.DateField(auto_now=False, auto_now_add=True)
    post_rating = models.DecimalField(max_digits=4, decimal_places=2, default=00.00)

    def __str__(self):
        return '{} {} {} {}'.format(self.game_name, self.post_header, self.game_rating, self.post_date)