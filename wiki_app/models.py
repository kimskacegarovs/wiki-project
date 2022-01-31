from django.db import models
from django.utils.text import slugify


class Page(models.Model):
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField(blank=True)
    view_counter = models.IntegerField(default=0)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
