from django.db import models

# Create your models here.
class File(models.Model):
    class Meta:
        unique_together = ('name', 'extension')

    name = models.CharField(max_length=25, null=False, blank=False)
    extension = models.CharField(max_length=6, null=False, blank=False)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '.' + self.extension
