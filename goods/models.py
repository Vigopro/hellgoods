import os
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Item(models.Model):

    def UPLOAD_TO(instance, filename):
        return 'goods/item/{}'.format(
            str(uuid.uuid4()) + os.path.splitext(filename)[1]
        )

    name = models.CharField(_('Name'), max_length=255)
    image = models.ImageField(_('Image'), upload_to=UPLOAD_TO)
    description = models.TextField(_('Description'))
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)

    created = models.DateTimeField(_('Created'), auto_now=False, auto_now_add=True)
    edited = models.DateTimeField(_('Edited'), auto_now=True)
    published = models.DateTimeField(_('Published'), default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-published']
        verbose_name = _('Item')
        verbose_name_plural = _('Items')


