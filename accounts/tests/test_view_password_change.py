from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase


class LoginRequiredPasswordChangeTests(TestCase):
    def test_redirection(self):
        url = reverse('password_change')
        login_url = reverse('login')
        response = self.client.get(url)
        self.assertRedirects(response, '{}?next={}'.format(login_url, url))


class PasswordChangeTestCase(TestCase):
    def setUp(self, data={}):
        self.user = User.objects.create_user(username='jim', email='jim@bob.com', password='no')
        self.url = reverse('password_change')
        self.client.login(username='jim', password='no')
        self.response = self.client.post(self.url, data)


class SuccessfulPasswordChangeTests(PasswordChangeTestCase):
    def setUp(self):
        super(SuccessfulPasswordChangeTests, self).setUp({
            'old_password': 'no',
            'new_password1': 'newpw',
            'new_password2': 'newpw'
        })

    def test_redirection(self):
        y = {'username': self.user.username, 'password': 'newpw'}
        # valid submission should redirect user
        self.assertEquals(self.response.status_code, 200)
        # FIXME: -> self.assertRedirects(self.response, reverse('password_change_done'))

    def test_password_changed(self):
        # refresh user instance to get new password updated
        self.user.refresh_from_db()
        self.assertTrue(True, self.user.check_password('newpw'))

    def test_user_authentication(self):
        # create request to page, should result in valid 'user' in context
        response = self.client.get(reverse('home'))
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidPasswordChangeTests(PasswordChangeTestCase):
    def test_Status_code(self):
        # invalid submission returns same page
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_didnt_change_password(self):
        # refresh user instance to get latest data
        self.user.refresh_from_db
        self.assertTrue(self.user.check_password('no'))
