from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Scripts(models.Model):
    title = models.CharField(max_length = 255)
    script = models.TextField(max_length = 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.first_name

