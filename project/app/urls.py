from django.conf import settings
from django.urls import re_path as url
from . import views
from .views import get_category_id

urlpatterns = [
    url(r'^api/product/$', views.ProductList.as_view()),
    url(r'^api/category/(?P<parent_id>\d+)/subcategories/$', views.SubcategoryList.as_view()),  # Moved up
    url(r'^api/category/$', views.CategoryList.as_view()),
    url(r'^api/category-id/(?P<category_name>[\w\-]+)/$', get_category_id, name='get_category_id'),

]