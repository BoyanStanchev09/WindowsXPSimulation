from django.contrib import admin

from folders.models import Folder, ShortCut


# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass

@admin.register(ShortCut)
class ShortCutAdmin(admin.ModelAdmin):
    pass