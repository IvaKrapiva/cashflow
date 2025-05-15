from django.test import TestCase
from .models import CashFlow, Status, Type, Category, Subcategory
from django.utils import timezone

class CashFlowTestCase(TestCase):
    def setUp(self):
        self.type = Type.objects.create(name='Пополнение')
        self.category = Category.objects.create(name='Маркетинг', type=self.type)
        self.subcategory = Subcategory.objects.create(name='Avito', category=self.category)
        self.status = Status.objects.create(name='Бизнес')

    def test_cashflow_creation(self):
        cashflow = CashFlow.objects.create(
            created_at=timezone.now().date(),
            status=self.status,
            type=self.type,
            category=self.category,
            subcategory=self.subcategory,
            amount=1000.50,
            comment='Тестовая запись'
        )
        self.assertEqual(cashflow.amount, 1000.50)
        self.assertEqual(cashflow.comment, 'Тестовая запись')

    def test_category_type_dependency(self):
        wrong_type = Type.objects.create(name='Списание')
        with self.assertRaises(Exception):
            CashFlow.objects.create(
                created_at=timezone.now().date(),
                status=self.status,
                type=wrong_type,
                category=self.category,
                subcategory=self.subcategory,
                amount=500
            )