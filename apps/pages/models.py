from typing import Any
from uuid import uuid4

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from tinymce.models import HTMLField


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
    title = models.CharField(_("Title"), max_length=255)
    content = HTMLField(_("Content"))
    slug = models.SlugField(_("Slug"), blank=True)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name=_("Tag"))
    timestamp = models.DateTimeField(_("Timestamp"), auto_now_add=True)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self) -> str:
        return self.title

    def generate_slug(self: "Page") -> None:
        """
        Generate a slug for the current instance based on the title attribute.

        Parameters:
            self (Page): The current instance of the class.

        Returns:
            None
        """
        self.slug = slugify(self.title)

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Save the object to the database.

        Args:
            *args: The positional arguments passed to the function.
            **kwargs: The keyword arguments passed to the function.

        Returns:
            None
        """
        if not self.slug:
            self.generate_slug()
        super().save(*args, **kwargs)
