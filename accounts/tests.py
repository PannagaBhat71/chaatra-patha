from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_signup_and_login_flow(self):
        # 1. Sign up a new student user
        signup_data = {
            'username': 'student_alpha',
            'email': 'alpha@example.com',
            'password1': 'AlphaPass1234!',
            'password2': 'AlphaPass1234!',
        }
        res = self.client.post(self.signup_url, data=signup_data, follow=True)
        self.assertEqual(res.status_code, 200)

        # Confirm user is in database
        self.assertTrue(UserModel.objects.filter(username='student_alpha').exists())
        user = UserModel.objects.get(username='student_alpha')
        self.assertEqual(user.email, 'alpha@example.com')

        # Log out
        self.client.post(self.logout_url)

        # 2. Log in using username
        login_res1 = self.client.post(self.login_url, {
            'username': 'student_alpha',
            'password': 'AlphaPass1234!',
        }, follow=True)
        self.assertEqual(login_res1.status_code, 200)
        self.assertTrue(login_res1.context['user'].is_authenticated)
        self.assertEqual(login_res1.context['user'].username, 'student_alpha')

        # Log out
        self.client.post(self.logout_url)

        # 3. Log in using email address
        login_res2 = self.client.post(self.login_url, {
            'username': 'alpha@example.com',
            'password': 'AlphaPass1234!',
        }, follow=True)
        self.assertEqual(login_res2.status_code, 200)
        self.assertTrue(login_res2.context['user'].is_authenticated)

        # Log out
        self.client.post(self.logout_url)

        # 4. Log in using case-insensitive email with trailing whitespace
        login_res3 = self.client.post(self.login_url, {
            'username': '  ALPHA@EXAMPLE.COM  ',
            'password': 'AlphaPass1234!',
        }, follow=True)
        self.assertEqual(login_res3.status_code, 200)
        self.assertTrue(login_res3.context['user'].is_authenticated)
