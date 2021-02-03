from django.apps import AppConfig


class TodolistConfig(AppConfig):
    name = 'apps.todolist'

    def ready(self):
        import apps.todolist.signals
