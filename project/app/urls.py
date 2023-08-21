from django.conf import settings
from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^api/product/$', views.ProductList.as_view()),
    url(r'^api/category/(?P<parent_id>\d+)/subcategories/$', views.SubcategoryList.as_view()),  # Moved up
    url(r'^api/category/$', views.CategoryList.as_view()),
    url(r'^api/category-id/$', views.get_parent_id_by_category_name),

]
