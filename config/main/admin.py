from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')
    list_display_links = ('id',)
    ordering = ('-id',)
    list_per_page = 20