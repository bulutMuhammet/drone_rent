from django.urls import path
from .views import RentedDroneListAPIView, RentedDroneRetrieveDestroyAPIView, \
    RentedDroneAllListAPIView

urlpatterns = [
    path('my-rented-drones', RentedDroneListAPIView.as_view(),
         name='rented-drone-list'),
    path('all-rented-drones', RentedDroneAllListAPIView.as_view(),
         name='all-rented-drone-list'),
    path('<int:pk>/', RentedDroneRetrieveDestroyAPIView.as_view(), name='rented-drone'),
]
