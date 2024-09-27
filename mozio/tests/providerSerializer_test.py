from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from mozio.serializers import ProviderSerializer

from .factories import (
    ProviderFactory,
    ProviderWithForeignFactory,
    ServiceAreaFactory,
)


class ProviderSerializer_Test(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.provider = ProviderWithForeignFactory.create()

    def test_that_a_provider_is_correctly_serialized(self):
        provider = self.provider
        serializer = ProviderSerializer
        serialized_provider = serializer(provider).data

        assert serialized_provider['id'] == provider.id
        assert serialized_provider['name'] == provider.name
        assert serialized_provider['email'] == provider.email
        assert serialized_provider['phone_number'] == provider.phone_number
        assert serialized_provider['language'] == provider.language
        assert serialized_provider['currency'] == provider.currency

        assert len(serialized_provider['serviceareas']) == provider.serviceareas.count()
