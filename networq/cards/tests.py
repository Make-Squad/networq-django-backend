from django.test import TestCase, SimpleTestCase
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Card

#test get/post
class CardsTest(TestCase):

  class PostTests(TestCase):
  
    def setUp(self):
        Card.objects.create(text='just a test')

    def test_text_content(self):
        post = Card.objects.get(id=1)
        expected_object_name = ''
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_list_view(self):
        response = self.client.get(reverse('cards'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'cards.html')
  
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