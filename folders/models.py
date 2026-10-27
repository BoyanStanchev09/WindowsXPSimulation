from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet, Q
from django.utils.text import slugify

from files.models import File


# Create your models here.
class Folder(models.Model):
    name = models.CharField(max_length=25, unique=True)
    parent_folder = models.OneToOneField(
        'Folder', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    @property
    def contents(self) -> tuple[QuerySet[File]|None, QuerySet[Folder]|None, QuerySet[ShortCut]|None]:
        files = File.objects.filter(folder=self)
        folders = Folder.objects.filter(parent_folder=self)
        shortcuts = ShortCut.objects.filter(to=self)
        return files, folders, shortcuts

    @property
    def location(self) -> str:
        names = []
        current = self
        visited = set()

        while current:
            marker = current.pk if current.pk else id(current)
            if marker in visited:
                raise ValueError("A folder cannot be its own ancestor.")
            visited.add(marker)
            names.append(current.name)
            current = current.parent_folder

        return 'C:\\' + '\\'.join(reversed(names))

    def clean(self):
        super().clean()
        current = self.parent_folder
        visited = {self.pk} if self.pk is not None else set()

        while current is not None:
            marker = current.pk if current.pk is not None else id(current)
            if marker in visited:
                raise ValidationError({
                    'parent_folder': 'A folder cannot be its own ancestor.'
                })
            visited.add(marker)
            current = current.parent_folder

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.location)
        super().save(*args, **kwargs)


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

    @property
    def type(self) -> str:
        if self.from_file is None:
             return 'file'
        elif self.from_folder is None:
            return 'folder'
        else:
            return 'unknown'

    def __str__(self):
        entity = ''
        location = ''

        if self.from_folder:
            entity = self.from_folder.name
        elif self.from_file:
            entity = self.from_file.name + '.' + self.from_file.extension

        if self.to:
            location = self.to.name
        else:
            location = 'Desktop'
        return f'{entity} shortcut to {location}'
