from django.urls import path

from dashboard.views import DashboardView, DashboardDroneRentView, AllRentsDashboardView, RentedDroneUpdateView

urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
    path('all-rents', AllRentsDashboardView.as_view(), name='all-rents'),
    path('new-drone-rent', DashboardDroneRentView.as_view(), name='new-drone-rent'),
    path('update-drone/<int:pk>', RentedDroneUpdateView.as_view(), name='update'),
]
