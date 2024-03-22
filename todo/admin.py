from django.contrib import admin
from .models import TodoModel

# Register your models here.
@admin.register(TodoModel)
class TodoAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'due_date', 'status']