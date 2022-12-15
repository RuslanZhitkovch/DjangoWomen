from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from website import settings
from .views import *


urlpatterns = [
    path('', index, name = 'home'),
    path('about/',about,name='about'),
    path('cats/<int:catid>/', categories),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)