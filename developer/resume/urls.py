from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index_view, name = 'index'),
    url(r'^work/$',views.work_view, name = 'work'),
    url(r'^contact/$',views.contact_view, name = 'contact'),
    ]
