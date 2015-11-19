from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Contacts.as_view(), name='list'),
]
