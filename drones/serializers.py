from rest_framework import serializers
from .models import RentedDrone

class RentedDroneSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="renting_user.first_name")
    user_last_name = serializers.CharField(source="renting_user.last_name")
    brand = serializers.CharField(source='drone.brand')
    model = serializers.CharField(source='drone.model')
    weight = serializers.DecimalField(source='drone.weight', max_digits=5,
                                      decimal_places=2)
    category = serializers.CharField(source='drone.get_category_display')

    class Meta:
        model = RentedDrone
        fields = ['id', 'user', 'user_last_name', 'brand','model', 'weight', 'category', 'start_date', 'end_date']
