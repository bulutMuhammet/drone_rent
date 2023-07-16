from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, UpdateView

from dashboard.forms import RentedDroneForm
from dashboard.permissions import IsOwnerOrAdmin, IsAdmin
from drones.models import Drone, RentedDrone


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'dashboard/index.html'


class AllRentsDashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'dashboard/all_rents.html'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)


class DashboardDroneRentView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('login')
    template_name = 'dashboard/rent_drone.html'
    form_class = RentedDroneForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save(commit=False)
        rent = form.instance
        rent.renting_user = self.request.user
        rent.save()
        messages.success(self.request,
                         "Kiralama işlemi başarılı.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,
                         [form.errors[i] for i in form.errors])
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drones = Drone.objects.all()
        form = self.form_class()
        context.update({"drones": drones, "form": form})
        return context


class RentedDroneUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/update_rent.html'
    form_class = RentedDroneForm
    model = RentedDrone
    success_url = reverse_lazy('index')
    permission_classes = [IsOwnerOrAdmin]

    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_superuser) and (
                self.get_object().renting_user != self.request.user):
            raise PermissionDenied()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request,
                         "Kiralama başarılıyla düzenlendi.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request,
                         [form.errors[i] for i in form.errors])
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        drones = Drone.objects.all()
        form = self.form_class()
        context.update({"drones": drones, "form": form})
        return context
