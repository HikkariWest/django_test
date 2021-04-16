from django.db import models
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
    CATEGORIES = [
        (0, 'Все'),
        (1, 'Игровые новости'),
        (2, 'Технологии'),
        (3, 'Софт'),
        (4, 'Новости киноиндустрии'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    category = models.SmallIntegerField(choices=CATEGORIES, default=0)
    publish = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True, blank=True)

    class Meta:
        ordering = ('id', 'publish')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
