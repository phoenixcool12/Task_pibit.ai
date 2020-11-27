
# Create your models here.
from django.db import models


class Image(models.Model):
    Image_Name = models.CharField(max_length=200)
    image_upload= models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.Image_Name
