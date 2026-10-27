from django.views.generic import DetailView

from files.models import File


# Create your views here.
class FileView(DetailView):
    model = File
    template_name = 'files/file.html'
    context_object_name = 'file'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
