from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required


class CacheMixin:
    def dispatch(self, *args, **kwargs):
        return cache_page(self.cache_timeout)(super().dispatch)(*args, **kwargs)
