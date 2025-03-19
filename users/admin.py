from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'email', 'is_active', 'date_joined')
    list_display_links = ('id', 'last_name', 'first_name')
    list_editable = ('is_active',)
    search_fields = ('last_name', 'first_name', 'email')
    list_filter = ('is_active', 'date_joined')
    readonly_fields = ('date_joined',)
    ordering = ('id',)
