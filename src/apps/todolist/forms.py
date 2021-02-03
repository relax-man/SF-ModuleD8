from django import forms
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

from apps.todolist.models import Category, TodoItem


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']

    def clean(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        slug = slugify(name)
        
        for category in Category.objects.all():
            if category.slug == slug:
                raise ValidationError(
                    {'name': 'Same name with other category'}
                )

        self.cleaned_data['slug'] = slug
        return super().clean(*args, **kwargs)


class TodoItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ['description', 'priority', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }
