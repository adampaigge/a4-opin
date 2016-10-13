from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from rules.contrib.views import PermissionRequiredMixin

from euth.projects import mixins
from euth.projects.models import Project

from . import forms, models


class DocumentCreateView(generic.CreateView, PermissionRequiredMixin):
    model = models.Document
    form_class = forms.DocumentCreateMultiForm

    def dispatch(self, *args, **kwargs):
        proj_slug = self.kwargs[self.slug_url_kwarg]
        self.project = Project.objects.get(slug=proj_slug)
        self.phase = self.project.active_phase
        self.module = self.phase.module if self.phase else None
        try:
            self.document = models.Document.objects.get(module=self.module)
        except ObjectDoesNotExist:
            self.document = None
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        kwargs.update({'module': self.module})
        kwargs.update({'document': self.document})
        return kwargs

    def get_success_url(self):
        return self.project.get_absolute_url()


class DocumentDetailView(generic.DetailView, mixins.ProjectMixin):
    model = models.Document

    def get_object(self):
        return models.Document.objects.filter(module=self.module).first()


class ParagraphDetailView(PermissionRequiredMixin, generic.DetailView):
    permission_required = 'euth_documents.view_paragraph'
    model = models.Paragraph

    @property
    def raise_exception(self):
        return self.request.user.is_authenticated()
