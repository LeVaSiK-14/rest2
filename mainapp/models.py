from django.db import models
from django.db.models import Avg, Min, Max, Sum


class Shop(models.Model):
    name = models.CharField(max_length=127)
    time_start = models.TimeField()
    time_end = models.TimeField()
    address = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name
        
    class Meta:
        db_table = 'shop'
        verbose_name = 'Магазин'
        verbose_name_plural = verbose_name + 'ы'

    @property
    def avg_ticket_price(self):
        return self.tickets.aggregate(Avg('price'))['price__avg']

    @property
    def min_ticket_price(self):
        return self.tickets.aggregate(Min('price'))['price__min']

    @property
    def max_ticket_price(self):
        return self.tickets.aggregate(Max('price'))['price__max']

    @property
    def sum_ticket_price(self):
        return self.tickets.aggregate(Sum('price'))['price__sum']

    @property
    def amount_ticket(self):
        return self.tickets.count()


class Ticket(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='tickets')
    name = models.CharField(max_length=127)
    price = models.PositiveIntegerField(default=0)
    replace_from = models.CharField(max_length=127)
    replace_to = models.CharField(max_length=127)


    def __str__(self) -> str:
        return f'Shop - {self.shop.name}, ticket {self.name}'

    class Meta:
        db_table = 'ticket'
        verbose_name = 'Билет'
        verbose_name_plural = verbose_name + 'ы'
