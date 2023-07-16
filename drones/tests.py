from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from drones.models import RentedDrone, Drone


class RentedDroneAllListAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_get_rented_drones_list(self):
        response = self.client.get(reverse('all-rented-drone-list'))
        self.assertEqual(response.status_code, 200)



class RentedDroneRetrieveDestroyAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.drone = Drone.objects.create(brand='Test Brand', model='Test Model', weight=1.0, category='kategori1')
        self.rented_drone = RentedDrone.objects.create(drone=self.drone, start_date='2023-01-01', end_date='2023-01-05', renting_user=self.user)

    def test_retrieve_rented_drone(self):
        url = reverse('rented-drone', kwargs={'pk': self.rented_drone.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_rented_drone(self):
        url = reverse('rented-drone', kwargs={'pk': self.rented_drone.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)



