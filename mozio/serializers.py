from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Provider, ServiceArea


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    provider = ProviderSerializer()

    class Meta:
        model = ServiceArea
        geo_field = 'geometry'
        fields = ('id', 'name', 'price', 'provider')
