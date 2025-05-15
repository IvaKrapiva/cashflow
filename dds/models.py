from django.db import models
from django.utils import timezone

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='categories')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Subcategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class CashFlow(models.Model):
    created_at = models.DateField(default=timezone.now)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.created_at} - {self.amount} руб."
    class Meta:
        verbose_name = 'Запись ДДС'
        verbose_name_plural = 'Записи ДДС'