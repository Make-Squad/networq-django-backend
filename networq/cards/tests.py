from django.test import TestCase
from django.contrib.auth import get_user_model

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
  