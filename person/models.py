from django.db import models
from django.utils.translation import ugettext as _


class Person(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    institution = models.CharField(_("Institution"), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = _("Person")
        verbose_name_plural = _("People")