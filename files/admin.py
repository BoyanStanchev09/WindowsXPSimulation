from django.contrib import admin

from files.models import File


# Register your models here.
@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Name', {'fields': ('name', 'extension')}),
        ('Content (optional)', {'fields': ('contents',)}),
        ('Location (optional)', {'fields': ('folder',)}),
    )
