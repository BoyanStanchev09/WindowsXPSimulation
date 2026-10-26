from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet, Q

from files.models import File


# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=25, unique=True)
    parent_folder = models.OneToOneField(
        'Folder', on_delete=models.SET_NULL, null=True, blank=True)
    short_cut = models.OneToOneField('ShortCut', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def contents(self) -> tuple[QuerySet[File]|None, QuerySet[Folder]|None, QuerySet[ShortCut]|None]:
        files = File.objects.filter(folder=self)
        folders = Folder.objects.filter(parent_folder=self)
        shortcuts = ShortCut.objects.filter(to=self)
        return files, folders, shortcuts

    @property
    def location(self) -> str:
        locations_str = self.name
        while self.parent_folder:
            locations_str = f'{self.parent_folder.name}\\{locations_str}'
        return 'C:\\' + locations_str

    def __str__(self):
        return self.name


class ShortCut(models.Model):
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=(Q(from_file__isnull=False, from_folder__isnull=True)
                           | Q(from_file__isnull=True, from_folder__isnull=False)),
                name="shortcut_either_file_or_folder"
            )
        ]

    to = models.ForeignKey(
        'Folder', on_delete=models.CASCADE, null=True, blank=True,
        related_name='placed_shortcuts',
    )   # if to is empty then the shortcut is to the desktop
    from_file = models.ForeignKey('files.File', on_delete=models.SET_NULL,
                                  related_name= 'file_shortcut', null=True, blank=True)
    from_folder = models.ForeignKey(
        'Folder', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='folder_shortcut',
    )

    def clean(self):
        super().clean()
        if (self.from_file is None) == (self.from_folder is None):
            raise ValidationError("Choose exactly one target: a file or a folder.")

    @property
    def to_desktop(self) -> bool:
        return self.to is None

    def __str__(self):
        entity = ''
        location = ''

        if self.from_folder:
            entity = self.from_folder.name
        elif self.from_file:
            entity = self.from_file.name

        if self.to:
            location = self.to.name
        else:
            location = 'Desktop'
        return f'{entity} shortcut to {location}'