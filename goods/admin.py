from django.contrib import admin

# Register your models here.
from .models import Item


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'link', 'published']
    search_fields = ['name', 'description']
    exclude = ['published']

    class Meta:
        model = Item

admin.site.register(Item, ItemModelAdmin)
