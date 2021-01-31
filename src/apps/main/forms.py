from django import forms


class FibForm(forms.Form):
    is_caching = forms.ChoiceField(choices=[(True, 'Yes'), (False, 'No')])
    fib_i = forms.IntegerField(help_text='It\'s need to be integer')
