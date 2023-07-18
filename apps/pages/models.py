from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class Tags(models.Model):
    id = models.UUIDField(_("Tag id"), primary_key=True, default=uuid4, unique=True, editable=False)
    tag_name = models.CharField(_("Tag name"), max_length=50)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.tag_name


class Page(models.Model):
    id = models.UUIDField(_("Page id"), primary_key=True, default=uuid4, unique=True, editable=False)
    title = models.CharField(_("(Title"), max_length=255)
    content = models.TextField(_("Content"))
    slug = models.SlugField(_("Slug"))
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self) -> str:
        return self.title
