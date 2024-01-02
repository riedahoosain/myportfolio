from django.contrib import admin
from .models import Item

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status","meal_type")
    list_filter = ("status",)
    search_fields = ("meal", "description","meal_type")

admin.site.register(Item, MenuItemAdmin)
