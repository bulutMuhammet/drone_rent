from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# kullandığım datatable.js kütüphanesi uygun olarak bazı kısımların düzenlenmesi
class RentedDronePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('recordsTotal', self.page.paginator.count),
            ('recordsFiltered', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))