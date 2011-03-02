from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^photos/$', 'photo.views.index'),
    (r'^photos/(?P<photo_id>\d+)/$', 'photo.views.show'),
    (r'^photos/(?P<photo_id>\d+)/results$', 'photo.views.results'),
    (r'^photos/(?P<photo_id>\d+)/vote$', 'photo.views.vote'),
    (r'^ranking/', 'photo.views.ranking'),
    # Example:
    # (r'^projetox/', include('projetox.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
