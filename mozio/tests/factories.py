from random import randint, uniform

import factory
from factory import LazyAttribute, LazyFunction, SubFactory, fuzzy
from factory.django import DjangoModelFactory
from faker import Factory

from mozio.models import Provider, ServiceArea

faker = Factory.create()


class ProviderFactory(DjangoModelFactory):
    class Meta:
        model = Provider

    name = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    email = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    phone_number = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    language = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    currency = LazyAttribute(lambda o: faker.text(max_nb_chars=255))


class ProviderWithForeignFactory(ProviderFactory):
    @factory.post_generation
    def serviceareas(obj, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for n in range(extracted):
                ServiceAreaFactory(provider=obj)
        else:
            number_of_units = randint(1, 10)
            for n in range(number_of_units):
                ServiceAreaFactory(provider=obj)


class ServiceAreaFactory(DjangoModelFactory):
    class Meta:
        model = ServiceArea

    provider = factory.SubFactory('mozio.tests.factories.ProviderFactory')
    name = LazyAttribute(lambda o: faker.text(max_nb_chars=255))
    price = LazyAttribute(lambda o: uniform(0.0, 10000))
    lng = LazyAttribute(lambda o: uniform(0, 10000))
    lat = LazyAttribute(lambda o: uniform(0, 10000))
