from django.conf.urls import include, url
from django.contrib import admin
from PyTuShare.views import hello

urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello),

]
