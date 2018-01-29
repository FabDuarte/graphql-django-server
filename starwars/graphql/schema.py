import graphene
import graphql_jwt
from .types import PeopleType, FilmType, PlanetType
from .mutations import CreateFilm
from starwars.models import People, Film, Planet
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.debug import DjangoDebug
from graphql import GraphQLError


class Query(graphene.ObjectType):
    all_planets = graphene.List(PlanetType)

    # Pagination & filter
    all_people = DjangoFilterConnectionField(PeopleType)
    all_films = DjangoFilterConnectionField(FilmType)
    my_films = DjangoFilterConnectionField(FilmType)

    # Debug
    debug = graphene.Field(DjangoDebug, name='__debug')

    def resolve_all_planets(self, info, **kwargs):
        return Planet.objects.all()

    def resolve_all_people(self, info, **kwargs):
        return People.objects.all()

    def resolve_all_films(self, info, **kwargs):
        return Film.objects.all()

    def resolve_my_films(self, info, **kwargs):
        if not info.context.user.is_authenticated:
            raise GraphQLError("Login required")
        else:
            return Film.objects.filter(owner=info.context.user)


class Mutations(graphene.ObjectType):
    create_film = CreateFilm.Field(Film)
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
