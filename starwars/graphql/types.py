import graphene
import datetime
from graphene_django.types import DjangoObjectType
from starwars.models import People, Transport, Species, Vehicle, Starship, Planet, Film
from graphene import Node


class PeopleType(DjangoObjectType):
    class Meta:
        model = People
        exclude_fields = ('created', 'edited')
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (Node,)


class FilmType(DjangoObjectType):
    age = graphene.Int(description="Current year - release year")

    class Meta:
        model = Film
        exclude_fields = ('created', 'edited')
        filter_fields = ('title', 'episode_id')
        interfaces = (Node,)

    def resolve_age(self, info):
        return datetime.datetime.now().year - self.release_date.year


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


# Connections
def connection_for_type(_type):
    class Connection(graphene.Connection):
        total_count = graphene.Int()

        class Meta:
            name = _type._meta.name + 'Connection'
            node = _type

        def resolve_total_count(self, args, context, info):
            return self.length

    return Connection


FilmType.Connection = connection_for_type(FilmType)
PeopleType.Connection = connection_for_type(PeopleType)
