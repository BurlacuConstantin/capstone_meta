from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenuView(TestCase):

    def setUp(self):
        self.item1 = Menu.objects.create(title="Grilled Cheese Sandwich", price=50, inventory=50)
        self.item2 = Menu.objects.create(title="White Sauce Pasta", price=100, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('items'))
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)