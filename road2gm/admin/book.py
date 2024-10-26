from django.contrib import admin
from ..models import book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified')
    ordering = ['-modified']


admin.site.register(book.Book, BookAdmin)
