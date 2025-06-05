# dictionary_app/admin.py

from django.contrib import admin
from .models import SearchLog

@admin.register(SearchLog)
class SearchLogAdmin(admin.ModelAdmin):
    list_display = ('word', 'searched_at')
    ordering = ('-searched_at',)
