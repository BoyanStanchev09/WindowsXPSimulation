from django.contrib import admin

from folders.models import Folder, ShortCut


# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    fields = ('name', 'parent_folder')

@admin.register(ShortCut)
class ShortCutAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Location', {'fields': ['to']}),
        ('From', {'fields': ('from_file', 'from_folder')}),
    )