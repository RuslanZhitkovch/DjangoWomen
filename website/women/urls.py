from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from website import settings
from .views import *


urlpatterns = [
    path('', index, name = 'home'),
    path('about/',about,name='about'),
    path('addpage/', addpage, name = 'add_page'),
    path('contact/', contact, name = 'contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/',show_post, name = 'post'),
    path('category/<int:cat_id>/',show_category, name = 'category'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)