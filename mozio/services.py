from django.contrib.gis.geos import Point
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, schema
from rest_framework.response import Response

from .models import ServiceArea
from .serializers import ServiceAreaSerializer

lng_param = openapi.Parameter('lng', openapi.IN_QUERY, description="Longitude", type=openapi.TYPE_NUMBER)
lat_param = openapi.Parameter('lat', openapi.IN_QUERY, description="Latitude", type=openapi.TYPE_NUMBER)


@swagger_auto_schema(method='get', manual_parameters=[lng_param, lat_param])
@api_view(['GET'])
def search_service_areas(request):
    try:
        lng = float(request.query_params.get('lng'))
        lat = float(request.query_params.get('lat'))
    except (TypeError, ValueError):
        return Response({'error': 'Invalid or missing lng/lat parameters'}, status=400)
    point = Point(lng, lat)
    service_areas = ServiceArea.objects.filter(geometry__contains=point)
    serializer = ServiceAreaSerializer(service_areas, many=True)
    return Response(serializer.data)
