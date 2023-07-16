from rest_framework import filters

# arama filtresi
class RentedDroneSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return ['renting_user__first_name','renting_user__last_name','drone__brand', 'drone__model', 'drone__weight', 'drone__category', 'start_date', 'end_date']