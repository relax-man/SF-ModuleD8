from django import template
from django.db.models.query import QuerySet

register = template.Library()

@register.filter(name='field_sum')
def field_sum(models_set: QuerySet[object], field_name: str) -> int:
    total_sum = 0
    for model in models_set:
        total_sum += getattr(model, field_name)
    return total_sum


@register.filter(name='get_percentage')
def get_percentage(dividend: int, divider: int) -> float:
    return round(dividend / divider * 100, 2)