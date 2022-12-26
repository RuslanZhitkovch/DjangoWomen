from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):           # для отображения больще полей в админ-панели
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)      # запятая нужна для того чтобы показать что это кортеж



admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)