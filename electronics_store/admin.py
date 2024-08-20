from django.contrib import admin
from .models import NetworkNode, Product


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'debt', 'created_at', 'supplier']
    list_filter = ['city']
    search_fields = ['name', 'city']
    actions = [clear_debt]
    readonly_fields = ['created_at']
    list_display_links = ['name', 'supplier']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'release_date', 'network_node']
    search_fields = ['name', 'model']
