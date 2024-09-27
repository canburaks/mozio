from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db.models import MultiPolygonField, PointField
from django.core.validators import MinValueValidator
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Provider(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "provider"

    def __str__(self):
        return self.name + " - " + self.email


class ServiceArea(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='serviceareas')
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(0.0)], null=True, blank=True, default=0.0)
    lng = models.FloatField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)

    geometry = MultiPolygonField()

    class Meta:
        db_table = "service_area"

    def __str__(self):
        return self.name
