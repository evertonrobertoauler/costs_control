from django.views.generic.edit import CreateView
from person.models import Person


class PersonCreateView(CreateView):
    model = Person