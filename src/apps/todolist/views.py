from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.todolist.models import Category, TodoItem, Priority
from apps.todolist.forms import CategoryForm, TodoItemForm


class CategoryListView(ListView):

    model = Category
    template_name = 'todolist/list_category.html'


class CategoryCreateView(CreateView):

    model = Category
    form_class = CategoryForm
    template_name = 'todolist/create_category.html'
    success_url = reverse_lazy('todolist:list_category')


class CategoryDeleteView(DeleteView):

    model = Category

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(reverse_lazy('todolist:list_category'))


class TodoItemListView(LoginRequiredMixin, ListView):

    model = TodoItem
    template_name = 'todolist/list_item.html'

    def get(self, request, *args, **kwargs):
        self.priority = kwargs.get('priority')
        self.extra_context = {
            'priority': Priority.objects.filter(level=self.priority),
            'priorities_list': Priority.objects.all()
        }
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.priority:
            return TodoItem.objects.filter(
                owner=self.request.user,
                priority__level=self.priority
            )
        return TodoItem.objects.filter(owner=self.request.user)


class TodoItemCreateView(LoginRequiredMixin, CreateView):

    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todolist/create_item.html'

    def form_valid(self, form : TodoItem):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        self._add_categories(form)
        return redirect(reverse_lazy('todolist:list_item'))

    def _add_categories(self, form : TodoItem):
        categories = form.cleaned_data.get('category')
        for book in Category.objects.filter(pk__in=categories):
            self.object.category.add(book)


class TodoItemToggleCompleteView(LoginRequiredMixin, UpdateView):

    model = TodoItem
    template_name = 'todolist/update_item.html'
    success_url = reverse_lazy('todolist:list_item')
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_completed = not self.object.is_completed
        self.object.save()
        return redirect(reverse_lazy('todolist:list_item'))


class TodoItemUpdateView(LoginRequiredMixin, UpdateView):

    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todolist/update_item.html'
    success_url = reverse_lazy('todolist:list_item')


class TodoItemDeleteView(LoginRequiredMixin, DeleteView):

    model = TodoItem

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(reverse_lazy('todolist:list_item'))
