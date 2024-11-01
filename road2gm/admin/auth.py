from django.contrib import admin
from ..models import auth


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    ordering = ('-modified',)


class RefreshTokenAdmin(admin.ModelAdmin):
    ordering = ('-created',)


admin.site.register(auth.User, UserAdmin)
admin.site.register(auth.RefreshToken, RefreshTokenAdmin)
