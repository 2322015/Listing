from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    GROUP=(('self', '個人'),
            ('Company', '会社'))

    group = models.TextField(
        verbose_name = '所属',
        choices=GROUP)
# Create your models here.
