from django import forms


class SearchForm(forms.Form):
    search_value = forms.CharField(label='Enter your request', max_length=20)


