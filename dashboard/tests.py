from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from dashboard.forms import RentedDroneForm
from drones.models import Drone, RentedDrone


class DashboardViewTest(TestCase):
    def test_dashboard_view(self):
        # Giriş yapmamış kullanıcıyı kontrol etmek için 302 HTTP durum kodunu bekleme (Yönlendirme)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

        # Giriş yapmış kullanıcıyı kontrol etmek için 200 HTTP durum kodunu bekleme (Başarılı)
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class AllRentsDashboardViewTest(TestCase):
    def test_all_rents_dashboard_view(self):
        # Giriş yapmamış kullanıcıyı kontrol etmek için 302 HTTP durum kodunu bekleme (Yönlendirme)
        response = self.client.get(reverse('all-rents'))
        self.assertEqual(response.status_code, 302)

        # Yönetici olarak giriş yapmış kullanıcıyı kontrol etmek için 200 HTTP durum kodunu bekleme (Başarılı)
        admin_user = User.objects.create_superuser(username='adminuser',
                                                   password='adminpass',
                                                   email='admin@example.com')
        self.client.login(username='adminuser', password='adminpass')
        response = self.client.get(reverse('all-rents'))
        self.assertEqual(response.status_code, 200)

        # Normal kullanıcıyı kontrol etmek için 403 HTTP durum kodunu bekleme (Erişim engellendi)
        user = User.objects.create_user(username='testuser', password='testpass',
                                        email='test@example.com')
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('all-rents'))
        self.assertEqual(response.status_code, 403)


class DashboardDroneRentViewTest(TestCase):
    def test_dashboard_drone_rent_view(self):
        # Giriş yapmamış kullanıcıyı kontrol etmek için 302 HTTP durum kodunu bekleme (Yönlendirme)
        response = self.client.get(reverse('new-drone-rent'))
        self.assertEqual(response.status_code, 302)

        # Giriş yapmış kullanıcıyı kontrol etmek için 200 HTTP durum kodunu bekleme (Başarılı)
        user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('new-drone-rent'))
        self.assertEqual(response.status_code, 200)

        # Formu geçerli verilerle göndererek başarılı bir talep yapın ve başarı mesajını kontrol edin
        drone = Drone.objects.create(brand="test brand", model="test", weight=100.0,
                                     category='kategori1')
        form_data = {'drone': drone.id, 'start_date': date.today(),
                     'end_date': date.today()}
        form_class = RentedDroneForm
        form = form_class(data=form_data)
        response = self.client.post(reverse('new-drone-rent'), data=form_data)
        self.assertEqual(response.status_code,
                         200)


class RentedDroneUpdateViewTest(TestCase):
    def test_rented_drone_update_view(self):
        user = User.objects.create_user(username='testuser', password='testpass', email='test@test.com')

        # Giriş yapmamış kullanıcıyı kontrol etmek için 302 HTTP durum kodunu bekleme (Yönlendirme)
        rented_drone = RentedDrone.objects.create(drone=Drone.objects.create(brand="test brand", model="test", weight=100.0,
                                     category='kategori1'), start_date=date.today(), end_date=date.today(), renting_user=user)
        response = self.client.get(reverse('update', args=[rented_drone.pk]))
        self.assertEqual(response.status_code, 302)

        # İzinli kullanıcıyı kontrol etmek için 200 HTTP durum kodunu bekleme (Başarılı)
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('update', args=[rented_drone.pk]))
        self.assertEqual(response.status_code, 200)

        # Formu geçerli verilerle göndererek başarılı bir talep yapın ve başarı mesajını kontrol edin
        drone = Drone.objects.create(brand="test brand", model="test", weight=100.0,
                                     category='kategori1')
        form_data = {'drone': drone.id, 'start_date': date.today(), 'end_date': date.today()}

        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('update', args=[rented_drone.pk]), data=form_data)
        self.assertEqual(response.status_code, 200)


