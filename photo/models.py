from django.db import models
from django.urls import reverse


class Photos(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to='media')
    using_count = models.IntegerField(default=0)
    gender = models.CharField(max_length=20)
    
    answer10 = models.IntegerField(default=0)
    answer20 = models.IntegerField(default=0)
    answer30 = models.IntegerField(default=0)
    answer11 = models.IntegerField(default=0)
    answer21 = models.IntegerField(default=0)
    answer31 = models.IntegerField(default=0)
    answer12 = models.IntegerField(default=0)
    answer22 = models.IntegerField(default=0)
    answer32 = models.IntegerField(default=0)
    answer13 = models.IntegerField(default=0)
    answer23 = models.IntegerField(default=0)
    answer33 = models.IntegerField(default=0)
    answer14 = models.IntegerField(default=0)
    answer24 = models.IntegerField(default=0)
    answer34 = models.IntegerField(default=0)
    