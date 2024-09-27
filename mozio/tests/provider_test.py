import json
from datetime import datetime

import factory
from django.core import management
from django.test import TestCase
from django.urls import reverse
from faker import Factory
from rest_framework import status
from rest_framework.test import APIClient

from ..models import Provider
from .factories import ProviderFactory, ServiceAreaFactory

faker = Factory.create()


class Provider_Test(TestCase):
    def setUp(self):
        self.api_client = APIClient()
        ProviderFactory.create_batch(size=3)

    def test_create_provider(self):
        """
        Ensure we can create a new provider object.
        """
        client = self.api_client
        provider_count = Provider.objects.count()
        provider_dict = factory.build(dict, FACTORY_CLASS=ProviderFactory)
        response = client.post(reverse('provider-list'), provider_dict)
        created_provider_pk = response.data['id']
        assert response.status_code == status.HTTP_201_CREATED
        assert Provider.objects.count() == provider_count + 1
        provider = Provider.objects.get(pk=created_provider_pk)

        assert provider_dict['name'] == provider.name
        assert provider_dict['email'] == provider.email
        assert provider_dict['phone_number'] == provider.phone_number
        assert provider_dict['language'] == provider.language
        assert provider_dict['currency'] == provider.currency

    def test_get_one(self):
        client = self.api_client
        provider_pk = Provider.objects.first().pk
        provider_detail_url = reverse('provider-detail', kwargs={'pk': provider_pk})
        response = client.get(provider_detail_url)
        assert response.status_code == status.HTTP_200_OK

    def test_fetch_all(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects
        """
        client = self.api_client
        response = client.get(reverse('provider-list'))
        assert response.status_code == status.HTTP_200_OK
        assert Provider.objects.count() == len(response.data)

    def test_delete(self):
        """
        Create 3 objects, do a fetch all call and check if you get back 3 objects.
        Then in a loop, delete one at a time and check that you get the correct number back on a fetch all.
        """
        client = self.api_client
        provider_qs = Provider.objects.all()
        provider_count = Provider.objects.count()

        for i, provider in enumerate(provider_qs, start=1):
            response = client.delete(reverse('provider-detail', kwargs={'pk': provider.pk}))
            assert response.status_code == status.HTTP_204_NO_CONTENT
            assert provider_count - i == Provider.objects.count()

    def test_update_correct(self):
        """
        Add an object. Call an update with 2 (or more) fields updated.
        Fetch the object back and confirm that the update was successful.
        """
        client = self.api_client
        provider_pk = Provider.objects.first().pk
        provider_detail_url = reverse('provider-detail', kwargs={'pk': provider_pk})
        provider_dict = factory.build(dict, FACTORY_CLASS=ProviderFactory)
        response = client.patch(provider_detail_url, data=provider_dict)
        assert response.status_code == status.HTTP_200_OK

        assert provider_dict['name'] == response.data['name']
        assert provider_dict['email'] == response.data['email']
        assert provider_dict['phone_number'] == response.data['phone_number']
        assert provider_dict['language'] == response.data['language']
        assert provider_dict['currency'] == response.data['currency']

    def test_update_name_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        provider = Provider.objects.first()
        provider_detail_url = reverse('provider-detail', kwargs={'pk': provider.pk})
        provider_name = provider.name
        data = {
            'name': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(provider_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert provider_name == Provider.objects.first().name

    def test_update_email_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        provider = Provider.objects.first()
        provider_detail_url = reverse('provider-detail', kwargs={'pk': provider.pk})
        provider_email = provider.email
        data = {
            'email': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(provider_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert provider_email == Provider.objects.first().email

    def test_update_phone_number_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        provider = Provider.objects.first()
        provider_detail_url = reverse('provider-detail', kwargs={'pk': provider.pk})
        provider_phone_number = provider.phone_number
        data = {
            'phone_number': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(provider_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert provider_phone_number == Provider.objects.first().phone_number

    def test_update_language_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        provider = Provider.objects.first()
        provider_detail_url = reverse('provider-detail', kwargs={'pk': provider.pk})
        provider_language = provider.language
        data = {
            'language': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(provider_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert provider_language == Provider.objects.first().language

    def test_update_currency_with_incorrect_value_outside_constraints(self):
        client = self.api_client
        provider = Provider.objects.first()
        provider_detail_url = reverse('provider-detail', kwargs={'pk': provider.pk})
        provider_currency = provider.currency
        data = {
            'currency': faker.pystr(min_chars=256, max_chars=256),
        }
        response = client.patch(provider_detail_url, data=data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert provider_currency == Provider.objects.first().currency
