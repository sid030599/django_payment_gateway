from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
 
@admin.register(Product)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['name', 'image','price','specification']