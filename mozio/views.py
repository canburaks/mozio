from rest_framework import viewsets
from rest_framework_gis.filters import InBBoxFilter

from .models import Provider, ServiceArea
from .serializers import ProviderSerializer, ServiceAreaSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    permission_classes = []
    filterset_fields = ['id', 'name', 'email', 'phone_number', 'language', 'currency', 'serviceareas']


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    bbox_filter_field = 'geometry'
    filter_backends = (InBBoxFilter,)  # Enables bounding box filtering
    filterset_fields = ['name']
