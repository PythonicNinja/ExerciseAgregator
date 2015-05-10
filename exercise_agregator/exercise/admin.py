from django.contrib import admin
from django.db import models

from .models import Exercise

from pagedown.widgets import AdminPagedownWidget


class ExerciseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Exercise, ExerciseAdmin)