from django.contrib import admin
from .models import Drone, RentedDrone


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'weight', 'category']
    search_fields = ['brand', 'model']
    list_filter = ['category']


@admin.register(RentedDrone)
class RentedDroneAdmin(admin.ModelAdmin):
    list_display = ['drone', 'start_date', 'end_date', 'renting_user']
    search_fields = ['drone__brand', 'drone__model', 'renting_user__username']
    list_filter = ['start_date', 'end_date']

