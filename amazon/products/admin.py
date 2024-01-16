from django.contrib import admin
from products.models import *  #tuzha application cha naav

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','name','price']

admin.site.register(Products_Table, ProductsAdmin) #ithe registeration hota