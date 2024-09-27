from datetime import datetime

import factory
from django.test import TestCase
from django.urls import reverse
from rest_framework import serializers
from rest_framework.test import APIRequestFactory

from mozio.serializers import ServiceAreaSerializer

from .factories import ServiceAreaFactory


class ServiceAreaSerializer_Test(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.serviceArea = ServiceAreaFactory.create()

    def test_that_a_serviceArea_is_correctly_serialized(self):
        serviceArea = self.serviceArea
        serializer = ServiceAreaSerializer
        serialized_serviceArea = serializer(serviceArea).data

        assert serialized_serviceArea['id'] == serviceArea.id
        assert serialized_serviceArea['name'] == serviceArea.name
        assert serialized_serviceArea['price'] == serviceArea.price
        assert serialized_serviceArea['lng'] == serviceArea.lng
        assert serialized_serviceArea['lat'] == serviceArea.lat
        assert serialized_serviceArea['geometry'] == serviceArea.geometry
