from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        pass


class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveSmallIntegerField()
    user = models.ForeignKey(AdvUser, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
