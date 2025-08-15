import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(verbose_name=_('ID'), default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated date'), auto_now=True)
    title = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    short_description = models.TextField(verbose_name=_('Short description'))
    content = models.TextField(verbose_name=_('Content'))
    poster_image = models.ImageField(verbose_name=_('Poster image'), default='posts/post-default.png', upload_to='posts/')
    tags = models.ManyToManyField(to='Tag', verbose_name=_('Tags'), related_name='tags', blank=True)
    is_active = models.BooleanField(verbose_name=_('Is active'), default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostComment(models.Model):
    id = models.UUIDField(verbose_name=_('ID'), default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated date'), auto_now=True)
    owner = models.ForeignKey(verbose_name=_('Author'), to=User, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(verbose_name=_('Reply to'), to='self', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(verbose_name=_('Comment'))

    def __str__(self):
        return f'{self.owner} - {self.created} - {self.text[:50]}'

    class Meta:
        ordering = ['-created']
        verbose_name = _('Post comment')
        verbose_name_plural = _('Post comments')


class Tag(models.Model):
    id = models.UUIDField(verbose_name=_('ID'), default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated date'), auto_now=True)
    name = models.CharField(verbose_name=_('Tag name'), max_length=10, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
