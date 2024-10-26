from django.contrib import admin
from ..models import auth


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    ordering = ('-modified',)


admin.site.register(auth.User, UserAdmin)
