from django.conf import settings
from django.urls import re_path as url
from . import views
from .views import get_category_id, NewProductAPIView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^api/product/$', views.ProductList.as_view()),
    url(r'^api/product/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^api/category/(?P<parent_id>\d+)/subcategories/$', views.SubcategoryList.as_view()),  # Moved up
    url(r'^api/category/$', views.CategoryList.as_view()),
    url(r'^api/category-id/(?P<category_name>[\w\-]+)/$', get_category_id, name='get_category_id'),
    url(r'^api/new-product/$', views.NewProductAPIView.as_view(), name='new-product-api'),
    url(r'^api/new-product-fields/$', views.get_form_fields, name='get-form-fields'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
