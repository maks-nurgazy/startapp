from django.db import models
from django.conf import settings


def get_product_upload_address(instance, path):
    return f'products/{instance.user}/${path}'


class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    cost = models.FloatField()
    price = models.FloatField()
    image = models.ImageField(upload_to=get_product_upload_address)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
