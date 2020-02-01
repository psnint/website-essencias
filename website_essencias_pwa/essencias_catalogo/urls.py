from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new
from django.conf.urls import url
from django.views.static import serve

from . import views

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    path('', views.index, name='home'),
    path('products', views.products, name='products'),
    path('collection/', views.collection, name='collection'),
    path('downloadCollection', views.download_collection, name='download_collection'),
    path('downloadProduct', views.download_product, name='download_product'),
    path('product_collection', views.product_collection, name='product_collection')
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
