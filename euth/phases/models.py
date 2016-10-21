from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

from euth.modules import models as modules_models

from . import content
from .validators import validate_content


class PhasesQuerySet(models.QuerySet):

    def active_phases(self):
        now = timezone.now()
        return self.filter(start_date__lte=now, end_date__gt=now)


class Phase(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    type = models.CharField(max_length=128, validators=[validate_content])
    module = models.ForeignKey(modules_models.Module, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    objects = PhasesQuerySet.as_manager()

    class Meta:
        ordering = ['type']

    def __str__(self):
        return '{} ({})'.format(self.name, self.type)

    def content(self):
        return content[self.type]

    def clean(self):
        if self.end_date and self.start_date:
            if self.end_date < self.start_date:
                raise ValidationError({
                    'end_date': _('End date can not be smaller'
                                  'than the start date.')
                })
        super().clean()

    @property
    def view(self):
        return content[self.type].view

    def has_feature(self, feature, model):
        return content[self.type].has_feature(feature, model)
