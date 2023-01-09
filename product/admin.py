from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display =['name']
    
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name']
    
    

    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['sku', 'description', 'name', 'mrp', 'weight', 'date_created', 'date_modified']