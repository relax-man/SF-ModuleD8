from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime

from apps.main.utils import CacheMixin


class IndexView(CacheMixin, TemplateView):

    template_name = 'main/base.html'
    extra_context = {
        'actual_time': datetime.now()
    }
    cache_timeout = 60
