from django.conf.urls import url
from django.urls.resolvers import URLPattern
from core import views

urlpatterns = [
    url(r'^products/$', views.ProductsApi),
    url(r'^products/([0-9]+)$', views.ProductsApi)
]