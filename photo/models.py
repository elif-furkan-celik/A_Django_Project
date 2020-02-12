from django.db import models


class Photos(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    using_count = models.IntegerField(default=0)
    date = models.DateTimeField("data published")

