from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from dashboard.permissions import IsAdmin, IsOwnerOrAdmin
from .filters import RentedDroneSearchFilter
from .models import RentedDrone
from .paginations import RentedDronePagination
from .serializers import RentedDroneSerializer


class RentedDroneAllListAPIView(generics.ListAPIView):
    serializer_class = RentedDroneSerializer
    queryset = RentedDrone.objects.select_related('drone')
    pagination_class = RentedDronePagination
    filter_backends = [RentedDroneSearchFilter, filters.OrderingFilter]
    permission_classes = [IsAuthenticated, IsAdmin]

class RentedDroneListAPIView(generics.ListAPIView):
    serializer_class = RentedDroneSerializer
    queryset = RentedDrone.objects.select_related('drone')
    pagination_class = RentedDronePagination
    filter_backends = [RentedDroneSearchFilter, filters.OrderingFilter]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = RentedDrone.objects.filter(renting_user=user)
        return queryset

class RentedDroneRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RentedDrone.objects.all()
    serializer_class = RentedDroneSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]