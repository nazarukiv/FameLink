from django.db import models
from django.template.defaultfilters import slugify
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
    is_published = models.BooleanField(
        choices=[(x[0], x[1]) for x in Status.choices],
        default=Status.DRAFT,
        verbose_name="Status"
    )
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    partner = models.OneToOneField("Partner", on_delete=models.SET_NULL, null=True, blank=True, related_name='par')
    photo = models.ImageField(
        upload_to="photos/",
        default=None,
        blank=True,
        null=True,
        verbose_name="Photo"
    )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Popular People'
        verbose_name_plural = 'Popular People'
        ordering = ['-time_created']
        indexes = [
            models.Index(fields=['time_created'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Partner(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')


