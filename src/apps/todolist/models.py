from django.db import models
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from model_utils import FieldTracker


class Category(models.Model):

    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=128)
    tasks_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.slug})'


class Priority(models.Model):

    PRIORITY_HIGH = 3
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 1

    level = models.PositiveIntegerField('level', default=PRIORITY_MEDIUM)
    tasks_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        if self.level == self.PRIORITY_HIGH:
            return 'High'
        elif self.level == self.PRIORITY_MEDIUM:
            return 'Medium'
        elif self.level == self.PRIORITY_LOW:
            return 'Low'


class TodoItem(models.Model):

    description = models.TextField('description')
    is_completed = models.BooleanField('is completed', default=False)
    created = models.DateTimeField('created', auto_now_add=True)
    updated = models.DateTimeField('updated', auto_now=True)

    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        related_name='tasks',
        default=2
    )
    tracker = FieldTracker(
        fields=['priority']
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    category = models.ManyToManyField(
        Category,
        related_name='tasks',
        blank=True
    )

    def __str__(self):
        return self.description[:20] + (self.description[20:] and '...')
