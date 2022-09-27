from rest_framework import serializers

from mainapp.models import Shop, Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'id', 'shop', 'name',
            'replace_from', 'replace_to',
            'price',
        )


class ShopSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(read_only=True, many=True)
    class Meta:
        model = Shop
        fields = (
            'id', 'name', 'time_start', 
            'time_end', 'address', 'tickets',
            'avg_ticket_price',
            'min_ticket_price',
            'max_ticket_price',
            'amount_ticket',
            'sum_ticket_price',
        )



