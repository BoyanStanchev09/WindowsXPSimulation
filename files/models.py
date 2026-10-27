from django.db import models
from django.utils.text import slugify

from files.choices import ExtensionChoices


# Create your models here.
class File(models.Model):
    class Meta:
        unique_together = ('name', 'extension')

    name = models.CharField(max_length=25, null=False, blank=False)
    extension = models.CharField(max_length=4, null=False, blank=False, choices=ExtensionChoices)
    contents = models.TextField(blank=True)    # not null because you will be able to change values
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    folder = models.ForeignKey(
        'folders.Folder', on_delete=models.SET_NULL, null=True, blank=True)
    short_cut = models.OneToOneField('folders.ShortCut', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def __str__(self):
        return self.name + '.' + self.extension

    @property
    def location(self):
        if not self.folder:
            return 'C:'
        return f'{self.folder.location}\\{self.folder.name}.{self.extension}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.location)
        super().save(*args, **kwargs)


