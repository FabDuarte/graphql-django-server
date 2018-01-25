import graphene
import datetime
from graphene_django.types import DjangoObjectType
from starwars.models import People, Transport, Species, Vehicle, Starship, Planet, Film
from graphene import resolve_only_args, Node


def connection_for_type(_type):
    class Connection(graphene.Connection):
        total_count = graphene.Int()

        class Meta:
            name = _type._meta.name + 'Connection'
            node = _type

        def resolve_total_count(self, args, context, info):
            return self.length

    return Connection


class PeopleType(DjangoObjectType):
    class Meta:
        model = People
        exclude_fields = ('created', 'edited')
        filter_fields = ('name',)
        interfaces = (Node,)


PeopleType.Connection = connection_for_type(PeopleType)


class TransportType(DjangoObjectType):
    class Meta:
        model = Transport


class SpecieType(DjangoObjectType):
    class Meta:
        model = Species


class VehicleType(DjangoObjectType):
    class Meta:
        model = Vehicle


class StarShipType(DjangoObjectType):
    class Meta:
        model = Starship


class PlanterType(DjangoObjectType):
    class Meta:
        model = Planet


class FilmType(DjangoObjectType):
    class Meta:
        model = Film
        exclude_fields = ('created', 'edited')
        filter_fields = ('title', 'episode_id')
        interfaces = (Node,)


FilmType.Connection = connection_for_type(FilmType)
