from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование товара'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание и характеристики товара'
    )
    price = models.FloatField(
        verbose_name='Цена'
    )

    def __str__(self):
        return self.name

