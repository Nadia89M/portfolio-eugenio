from django.db import models
from datetime import datetime
from categories.models import Category

# Create your models here.
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True , blank=True)
    title = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    published_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
