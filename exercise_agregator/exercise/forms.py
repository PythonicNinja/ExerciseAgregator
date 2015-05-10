# -*- coding: utf-8 -*-
# CREATED ON DATE: 10.05.15
from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False)