from django.db import models


# Product models

class Product(models.Model):

    LIVE=0
    DELETE=0
    DELETE_CHOICES=((LIVE,"live"),(DELETE,"delete"))

    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    images=models.ImageField(upload_to="media/")
    priority=models.IntegerField(default=0)

    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title