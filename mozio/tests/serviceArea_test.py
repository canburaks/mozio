import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import ServiceArea
from .factories import ProviderFactory, ServiceAreaFactory

faker = Factory.create()


class ServiceArea_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        ServiceAreaFactory.create_batch(size=3)
        self.provider = ProviderFactory.create()

    def test_create_serviceArea(self):
        """
        Ensure we can create a new serviceArea object.
        """
        client = self.api_client
        serviceArea_count = ServiceArea.objects.count()
        serviceArea_dict = factory.build(dict, FACTORY_CLASS=ServiceAreaFactory, provider=self.provider.id)
        response = client.post(reverse('serviceArea-list'), serviceArea_dict)
        created_serviceArea_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert ServiceArea.objects.count() == serviceArea_count + 1
        serviceArea = ServiceArea.objects.get(pk=created_serviceArea_pk)

        assert serviceArea_dict['name'] == serviceArea.name
        assert serviceArea_dict['price'] == serviceArea.price
        assert serviceArea_dict['lng'] == serviceArea.lng
        assert serviceArea_dict['lat'] == serviceArea.lat
        assert serviceArea_dict['geometry'] == serviceArea.geometry

    def test_get_one(self):
        client = self.api_client
        serviceArea_pk = ServiceArea.objects.first().pk
        serviceArea_detail_url = reverse('serviceArea-detail', kwargs={'pk': serviceArea_pk})
        response = client.get(serviceArea_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('serviceArea-list'))
        assert response.status_code == status.HTTP_200_OK
        assert ServiceArea.objects.count() == len(response.data)

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        serviceArea_qs = ServiceArea.objects.all()
        serviceArea_count = ServiceArea.objects.count()

        for i, serviceArea in enumerate(serviceArea_qs, start=1):
            response = client.delete(reverse('serviceArea-detail', kwargs={'pk': serviceArea.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert serviceArea_count - i == ServiceArea.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        serviceArea_pk = ServiceArea.objects.first().pk
        serviceArea_detail_url = reverse('serviceArea-detail', kwargs={'pk': serviceArea_pk})
        serviceArea_dict = factory.build(dict, FACTORY_CLASS=ServiceAreaFactory, provider=self.provider.id)
        response = client.patch(serviceArea_detail_url, data=serviceArea_dict)
        assert response.status_code == status.HTTP_200_OK

        assert serviceArea_dict['name'] == response.data['name']
        assert serviceArea_dict['price'] == response.data['price']
        assert serviceArea_dict['lng'] == response.data['lng']
        assert serviceArea_dict['lat'] == response.data['lat']
        assert serviceArea_dict['geometry'] == response.data['geometry']

    def test_update_price_with_incorrect_value_data_type(self):
        client = self.api_client
        serviceArea = ServiceArea.objects.first()
        serviceArea_detail_url = reverse('serviceArea-detail', kwargs={'pk': serviceArea.pk})
        serviceArea_price = serviceArea.price
        data = {
            'price': faker.pystr(),
        }
        response = client.patch(serviceArea_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert serviceArea_price == ServiceArea.objects.first().price

    def test_update_lng_with_incorrect_value_data_type(self):
        client = self.api_client
        serviceArea = ServiceArea.objects.first()
        serviceArea_detail_url = reverse('serviceArea-detail', kwargs={'pk': serviceArea.pk})
        serviceArea_lng = serviceArea.lng
        data = {
            'lng': faker.pystr(),
        }
        response = client.patch(serviceArea_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert serviceArea_lng == ServiceArea.objects.first().lng

    def test_update_lat_with_incorrect_value_data_type(self):
        client = self.api_client
        serviceArea = ServiceArea.objects.first()
        serviceArea_detail_url = reverse('serviceArea-detail', kwargs={'pk': serviceArea.pk})
        serviceArea_lat = serviceArea.lat
        data = {
            'lat': faker.pystr(),
        }
        response = client.patch(serviceArea_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert serviceArea_lat == ServiceArea.objects.first().lat

    def test_update_name_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        serviceArea = ServiceArea.objects.first()
        serviceArea_detail_url = reverse('serviceArea-detail', kwargs={'pk': serviceArea.pk})
        serviceArea_name = serviceArea.name
        data = {
            'name': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(serviceArea_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert serviceArea_name == ServiceArea.objects.first().name

    def test_update_geometry_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        serviceArea = ServiceArea.objects.first()
        serviceArea_detail_url = reverse('serviceArea-detail', kwargs={'pk': serviceArea.pk})
        serviceArea_geometry = serviceArea.geometry
        data = {
            'geometry': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(serviceArea_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert serviceArea_geometry == ServiceArea.objects.first().geometry
