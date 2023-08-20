from django.conf import settings
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^api/product/$', views.ProductList.as_view()),

]
