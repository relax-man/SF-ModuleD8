from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.cache import cache
import time

from apps.main.forms import FibForm


class IndexView(View):

    def get(self, request):
        context = {'fib_form': FibForm}
        return render(request, 'main/base.html', context)

    def post(self, request):
        form = FibForm(request.POST)
        if form.is_valid():
            return render(request, 'main/fib.html', self._get_context(form))
        
        context = {'fib_form': form}
        return render(request, 'main/base.html', context)

    def _get_context(self, form : FibForm):
        is_caching = form.cleaned_data.get('is_caching')
        fib_i = form.cleaned_data.get('fib_i')
        start_time = time.time()
        if is_caching == 'True':
            fib_number = self._fib_caching(fib_i)
        else:
            fib_number = self._fib(fib_i)
        elapsed_time = (time.time() - start_time) * 1000
        return {
            'fib_form': form,
            'fib_number': fib_number,
            'elapsed_time': elapsed_time
        }

    def _fib(self, n : int):
        if n in [0, 1]:
            return n
        return self._fib(n-1) + self._fib(n-2)
    
    def _fib_caching(self, n : int):
        if n in [0, 1]:
            return n
        if f'fib_{n}' in cache:
            return cache.get(f'fib_{n}')
        fib_value = self._fib_caching(n-1) + self._fib_caching(n-2)
        cache.set(f'fib_{n}', fib_value, 60)
        return fib_value
