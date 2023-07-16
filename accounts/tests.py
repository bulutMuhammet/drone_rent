from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class LoginViewTest(TestCase):
    def test_login(self):
        # Önceden oturum açmış bir kullanıcı oluşturulur
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('login'))
        # Kullanıcı başarılı bir şekilde giriş yapmış olduğu için yönlendirilir
        self.assertRedirects(response, reverse('index'))





class LogoutViewTest(TestCase):
    def test_logout(self):
        # Önceden oturum açmış bir kullanıcı oluşturulur
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('logout'))

        # Kullanıcı başarılı bir şekilde oturumdan çıkar
        self.assertRedirects(response, reverse('login'))

        # Kullanıcının oturumu kapatıldığından emin olmak için session kontrolü yapılır
        self.assertNotIn('_auth_user_id', self.client.session)




class RegisterViewTest(TestCase):

    def test_valid_form_registers_user(self):
        response = self.client.post(reverse('register'), {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        # Geçerli form nedeniyle kullanıcı kaydedilir
        self.assertRedirects(response, reverse('login'))
        # Kullanıcı kaydedilmiş durumda olmalıdır
        self.assertTrue(User.objects.filter(email='johndoe@example.com').exists())

