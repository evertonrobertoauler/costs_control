from django.conf.urls import patterns, url
from person.views import (
    PersonListView,
    PersonCreateView,
    PersonUpdateView,
    PersonDeleteView,
)

urlpatterns = patterns(
    '',
    url(r'^$', PersonListView.as_view(), name='person-list'),
    url(r'^add/$', PersonCreateView.as_view(), name='person-add'),
    url(r'^edit/', PersonUpdateView.as_view(), name='person-edit'),
    url(r'^delete/', PersonDeleteView.as_view(), name='person-edit'),
)