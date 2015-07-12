from django.conf.urls import include, url,patterns

from PyShareSelect.views import hello

urlpatterns = patterns('',
    url(r'^$', hello),
)


