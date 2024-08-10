from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class People(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft Article'
        PUBLISHED = 1, "Actual Article"

    title = models.CharField(max_length=250, blank=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['time_created'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
