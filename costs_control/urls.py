from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    # url(r'^$', 'costs_control.views.home', name='home'),
    url(r'^person/', include('person.urls', app_name='person')),
    url(r'^cost/', include('cost.urls', app_name='cost')),
)
