from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.dispatch import receiver
from collections import Counter
from django.db.models.query import QuerySet

from apps.todolist.models import Category, Priority, TodoItem


def _change_category_tasks_count(category_set: QuerySet[Category], diff: int):
    for category in category_set:
        category.tasks_count += diff
        category.save()


def _change_priority_tasks_count(priority: Priority, diff: int=0):
    priority.tasks_count = priority.tasks.count() + diff
    priority.save()


@receiver(post_save, sender=TodoItem)
def task_post_saved(sender, instance, created, **kwargs):
    new_priority = instance.priority
    old_priority_pk = instance.tracker.previous('priority')

    _change_priority_tasks_count(new_priority)
    if old_priority_pk and old_priority_pk != new_priority.pk:
        _change_priority_tasks_count(Priority.objects.get(pk=old_priority_pk))


@receiver(pre_delete, sender=TodoItem)
def task_pre_deleted(sender, instance, **kwargs):
    _change_priority_tasks_count(instance.priority, -1)
    _change_category_tasks_count(instance.category.all(), -1)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_added_to_category(sender, instance, action, pk_set, **kwargs):
    if action != 'post_add':
        return

    _change_category_tasks_count(Category.objects.filter(id__in=pk_set), 1)


@receiver(m2m_changed, sender=TodoItem.category.through)
def task_removed_from_category(sender, instance, action, pk_set, **kwargs):
    if action != 'post_remove':
        return

    _change_category_tasks_count(Category.objects.filter(id__in=pk_set), -1)
