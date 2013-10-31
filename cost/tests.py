from django.test import TestCase
from cost.models import Cost, CostPart
from model_mommy.mommy import make


class CostTest(TestCase):

    def test_total_value(self):
        c = make(Cost)
        make(CostPart, _quantity=5, cost=c, value=2)

        self.assertEqual(float(5 * 2), c.total_value)