from queue import ShutDown

from django.utils import timezone
from django.views.generic import TemplateView, RedirectView

from files.models import File
from folders.models import Folder, ShortCut


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'folders': Folder.objects.filter(parent_folder__isnull=True),
            'files': File.objects.filter(folder__isnull=True),
            'shortcuts': ShortCut.objects.filter(to__isnull=True),
        })
        return context


class RestartView(RedirectView):
    pattern_name = 'index'


class ShutDownView(TemplateView):
    template_name = 'shutdown.html'
