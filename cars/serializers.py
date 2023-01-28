from rest_framework import serializers

from .models import Car, Reservation


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability'
        )

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')

        if request.user and not request.user.is_staff:
            fields.pop('availability')
            fields.pop('plate_number')


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = (
            'id',
            'customer',
            'car',
            'start_date',
            'end_date'
        )

        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Reservation.objects.all(),
                fields=('customer', 'start_date', 'end_date'),
                message=("You already have a reservation between the dates")
            )
        ]
