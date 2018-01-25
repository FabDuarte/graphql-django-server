import graphene
from .types import PeopleType, VehicleType, FilmType
from starwars.models import People, Vehicle, Film
from graphene_django.filter import DjangoFilterConnectionField
from graphene import resolve_only_args, Node
from graphene_django.debug import DjangoDebug


class Query(graphene.ObjectType):
    all_people = DjangoFilterConnectionField(PeopleType)
    all_films = DjangoFilterConnectionField(FilmType)

    people = Node.Field(PeopleType)
    films = Node.Field(FilmType)
    viewer = graphene.Field(lambda: Query)
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_viewer(self, *args, **kwargs):
        return self

    def resolve_all_people(self, info, **kwargs):
        return People.objects.all()

    def resolve_all_films(self, info, **kwargs):
        return Film.objects.all()


schema = graphene.Schema(query=Query)
