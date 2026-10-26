from django.contrib import admin

from folders.models import Folder


# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    pass