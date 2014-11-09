from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^top/$', 'testapp.views.main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^yakiniku/$', 'testapp.views.harami'),
)
