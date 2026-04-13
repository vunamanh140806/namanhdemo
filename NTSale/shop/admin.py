from django.contrib import admin
from .models import Categories, Suppliers, Products

admin.site.register(Categories)

@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ('CompanyName', 'Country')

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('ProductName', 'OldPrice', 'UnitPrice', 'UnitsInStock', 'Discontinued')
    list_filter = ('Category', 'Supplier')
