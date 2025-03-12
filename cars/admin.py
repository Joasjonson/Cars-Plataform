from django.contrib import admin
from cars.models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'id')
    list_per_page = 25

admin.site.register(Brand, BrandAdmin)


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'user', 'model_year', 'value', 'id')
    list_display_links = ('name', 'brand', 'model_year', 'value', 'id')
    search_fields = ('name', 'brand', 'factory_year', 'model_year', 'value', 'id')
    list_per_page = 25

admin.site.register(Car, CarAdmin)
