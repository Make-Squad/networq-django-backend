from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.urls import reverse

#user should be able to login if they have not registered

#user should be able to signup

#user should be able to login

#user should be able to logout

#test index page

#page should load

#test get/post
class UsersTest(TestCase):

  def test_create_user(self):
    User = get_user_model()
    user = User.objects.create_user(
      email='user@user.com',
      password='password'
      )
    self.assertEqual(user.email, 'user@user.com')
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_superuser)
    try:
      self.assertIsNone(user.username)
    except AttributeError:
      pass
    with self.assertRaises(TypeError):
      User.objects.create_user()
    with self.assertRaises(TypeError):
      User.objects.create_user(email='')
    with self.assertRaises(ValueError):
      User.objects.create_user(email='', password='password')
  
class HomePageTests(SimpleTestCase):
  
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Homepage</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')