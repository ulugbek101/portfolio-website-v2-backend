import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    content = models.TextField(verbose_name=_('Content'))
    is_active = models.BooleanField(verbose_name=_('Is active'), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
