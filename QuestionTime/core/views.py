from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class IndexTemplateView(LoginRequiredMixin, TemplateView):
    """
    Render the homepage template.

    * Only authenticated users.
    """

    def get_template_names(self):
        return 'index.html'
