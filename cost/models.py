from django.db import models
from django.db.models import Sum
from person.models import Person
from datetime import date
from django.utils.translation import ugettext as _

COST_TYPE = (
    (1, _('Fixed')),
    (2, _('Others')),
)

YES_NO = (
    (True,  _('Yes')),
    (False, _('No')),
)


class Cost(models.Model):
    debtor = models.ForeignKey(Person, verbose_name=_('Debtor'), related_name='debtor_cost')
    creditor = models.ForeignKey(Person, verbose_name=_('Creditor'), related_name='creditor_cost')
    cost_type = models.SmallIntegerField(_('Type'), choices=COST_TYPE)
    description = models.CharField(_('Description'), max_length=100)
    cost_date = models.DateField(_('Date'), default=date.today())

    @property
    def total_value(self):
        return float(self.costpart_set.aggregate(t=Sum('value'))['t'])
    
    def __str__(self):
        return self.description

    class Meta:
        ordering = ["-cost_date"]
        verbose_name = _("Cost")
        verbose_name_plural = _("Costs")


class CostPart(models.Model):
    cost = models.ForeignKey(Cost, verbose_name=_("Cost"))
    number = models.PositiveIntegerField(_("Number"))
    expiration = models.DateField(_("Expiration"))
    paid = models.BooleanField(_("Paid"), choices=YES_NO)
    value = models.DecimalField(_("Value"), max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.number)

    class Meta:
        ordering = ["number"]
        verbose_name = _("Cost Part")
        verbose_name_plural = _("Cost Parts")