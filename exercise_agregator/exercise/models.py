
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from djorm_pgfulltext.fields import VectorField
from djorm_pgfulltext.models import SearchManager

from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Exercise(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Created by'))
    title = models.CharField(max_length=155, verbose_name=_('Title'))
    slug = models.SlugField(_("Slug"), unique_for_date='created', default='')

    description = models.TextField(verbose_name=_('Description'))

    solution_text = models.TextField(verbose_name=_('Text solution'))
    solution_file = models.FileField(verbose_name=_('File solution'), blank=True, null=True)

    search_index = VectorField()

    objects = SearchManager(
        fields=('title', 'description'),
        config='pg_catalog.english',
        search_field='search_index',
        auto_update_search_field = True
    )

    tags = TaggableManager()

    def __unicode__(self):
        return self.title