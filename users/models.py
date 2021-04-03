from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from django.db import models


# Create your models here.
class User(AbstractUser):

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f'{self.username}'
