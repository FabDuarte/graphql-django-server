import graphene
from .types import PeopleType, FilmType
from .mutations import CreateFilm
from starwars.models import People, Film
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug


class Query(graphene.ObjectType):
    all_people = DjangoFilterConnectionField(PeopleType)
    all_films = DjangoFilterConnectionField(FilmType)
    my_films = DjangoFilterConnectionField(FilmType)

    """people = Node.Field(PeopleType)
    films = Node.Field(FilmType)
    """

    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_viewer(self, *args, **kwargs):
        return self

    def resolve_all_people(self, info, **kwargs):
        return People.objects.all()

    def resolve_all_films(self, info, **kwargs):
        return Film.objects.all()

    def resolve_my_films(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            return Film.objects.none()
        else:
            return Film.objects.filter(owner=info.context.user)


class Mutations(graphene.ObjectType):
    create_film = CreateFilm.Field(Film)


schema = graphene.Schema(query=Query, mutation=Mutations)
