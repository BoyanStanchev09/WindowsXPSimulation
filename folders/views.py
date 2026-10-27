from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from files.models import File
from folders.models import Folder, ShortCut


# Create your views here.
class FolderView(TemplateView):
    template_name = 'folders/folder.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        if slug:
            folder = get_object_or_404(Folder, slug=slug)
            files = File.objects.filter(folder=folder)
            folders = Folder.objects.filter(parent_folder=folder)
            shortcuts = ShortCut.objects.filter(to=folder)
        else:
            folder = None
            files = File.objects.filter(folder=None)
            folders = Folder.objects.filter(parent_folder=None)
            shortcuts = ShortCut.objects.filter(to=None)

        context.update({
            'curr_folder': folder,
            'files': files,
            'folders': folders,
            'shortcuts': shortcuts,
        })
        return context
