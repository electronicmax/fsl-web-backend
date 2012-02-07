from django.conf.urls.defaults import patterns, include, url
import public_www.views as v
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',  url(r'^post_email$', v.post_email))
