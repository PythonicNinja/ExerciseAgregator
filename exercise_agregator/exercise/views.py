
from django.views.generic import ListView, DetailView

from .models import Exercise
from .forms import SearchForm


class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercise/list.html'
    paginate_by = 10
    form_class = SearchForm

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Exercise.objects.search(form.cleaned_data['search'])
        return Exercise.objects.all()


class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'exercise/detail.html'
    lookup_field = 'slug'
    context_object_name = 'exercise'

