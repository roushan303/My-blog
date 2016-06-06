from django.conf.urls import url
from django.contrib import admin
from .views import (
	blog_list,
	blog_create,
	blog_detail,
	blog_update,
	blog_delete,
	)


urlpatterns = [
	url(r'^$', blog_list, name='list'),
    url(r'^create/$', blog_create),
    url(r'^(?P<slug>[\w-]+)/$', blog_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', blog_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', blog_delete),
]
