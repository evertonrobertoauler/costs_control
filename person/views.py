from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from person.models import Person


class PersonListView(ListView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    success_url = '/person/'


class PersonUpdateView(UpdateView):
    model = Person
    success_url = '/person/'
    template_name_suffix = '_update_form'


class PersonDeleteView(DeleteView):
    model = Person
    success_url = '/person/'
