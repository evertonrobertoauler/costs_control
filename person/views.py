from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from person.models import Person
from django.core.urlresolvers import reverse_lazy


class PersonListView(ListView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    success_url = reverse_lazy('person-list')


class PersonUpdateView(UpdateView):
    model = Person
    success_url = reverse_lazy('person-list')
    template_name_suffix = '_update_form'


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('person-list')