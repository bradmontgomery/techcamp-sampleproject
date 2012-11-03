from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^blog/(?P<post_slug>.+)/$',
        'blog.views.display_post',
        name='display_post'),
    url(r'^admin/', include(admin.site.urls)),
)
