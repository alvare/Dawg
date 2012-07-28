from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dawg/', include('dawg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'weblog.views.index'),
    (r'^(\d+)$', 'weblog.views.article'),

    (r'^captchion', 'captchion.views.play'),
    (r'^refresh', 'captchion.views.refresh'),
    (r'^reset', 'captchion.views.reset'),
    (r'^submit', 'captchion.views.submit'),
)
