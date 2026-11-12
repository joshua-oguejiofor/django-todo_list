from django.contrib import admin
from .models import Todo

# Registering the Todo model makes it manageable through /admin/
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    # Columns shown in the admin list view
    list_display = ('title', 'completed', 'created_at')
    # Adds a filter sidebar in the admin list view
    list_filter = ('completed',)
    # Adds a search box that searches the title field
    search_fields = ('title',)
