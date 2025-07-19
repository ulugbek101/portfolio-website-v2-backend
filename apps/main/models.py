import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(verbose_name=_('Title'), max_length=255, unique=True)
    content = models.TextField(verbose_name=_('Content'))
    poster_image = models.ImageField(default='posts/post-default.png', upload_to='posts/')
    is_active = models.BooleanField(verbose_name=_('Is active'), default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostComment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(verbose_name=_('Author'), to=User, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(verbose_name=_('Reply to'), to='self', on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(verbose_name=_('Comment'))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.owner} - {self.created} - {self.text[:50]}'

    class Meta:
        ordering = ['-created']
        verbose_name = _('Post comment')
        verbose_name_plural = _('Post comments')
