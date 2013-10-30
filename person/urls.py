from django.conf.urls import patterns, url
from person.views import PersonCreateView

urlpatterns = patterns(
    '',
    url(r'^$', PersonCreateView.as_view(), name='person_create'),
)