from mainapp.serializers import (
    Shop, ShopSerializer,
    Ticket, TicketSerializer
)
from django.db.models import Sum
from rest_framework.viewsets import ModelViewSet


class ShopView(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class TicketView(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

