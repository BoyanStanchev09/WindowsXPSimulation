from django.db import models
from django.db.models import QuerySet

from files.models import File


# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=25, unique=True)
    parent_folder = models.OneToOneField('Folder', on_delete=models.CASCADE)

    @property
    def contents(self) -> tuple[QuerySet[File]|None, QuerySet[Folder]|None]:
        files = File.objects.filter(folder=self)
        folders = Folder.objects.filter(parent_folder=self)
        return files, folders

    @property
    def location(self) -> str:
        locations_str = self.name
        while self.parent_folder:
            locations_str = f'{self.parent_folder.name}/{locations_str}'
        return locations_str

    def __str__(self):
        return self.name