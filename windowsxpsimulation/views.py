from django.views.generic import TemplateView, RedirectView


class IndexView(TemplateView):
    template_name = 'index.html'


class RestartView(RedirectView):
    pattern_name = 'index'


class ShutDownView(TemplateView):
    template_name = 'shutdown.html'
