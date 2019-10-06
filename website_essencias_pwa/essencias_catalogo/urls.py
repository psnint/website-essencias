from django.urls import path
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

from . import views

urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    path('', views.index, name='home'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)