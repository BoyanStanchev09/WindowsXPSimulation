from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, RedirectView

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

class ShortCutRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        shortcut = get_object_or_404(ShortCut, pk=kwargs['pk'])
        target_folder = shortcut.from_folder

        if target_folder is None and shortcut.from_file is not None:
            target_folder = shortcut.from_file.folder

        if target_folder is None:
            return reverse('folder_root')

        return reverse('folder_view', kwargs={'slug': target_folder.slug})

