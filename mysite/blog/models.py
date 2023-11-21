from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):



    class Meta:
        __default_sorting = '-publish'
        ordering = [__default_sorting]
        indexes = [
            models.Index(fields=[__default_sorting])
        ]


    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    def __str__(self):
        return self.title