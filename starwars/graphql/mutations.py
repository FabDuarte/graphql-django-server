import graphene
import json
import datetime
from .types import FilmType
from ..models import Film


class CreateFilm(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        episode_id = graphene.Int()

    form_error = graphene.String()
    film = graphene.Field(lambda: FilmType)

    @staticmethod
    def mutate(self, info, title, episode_id):
        if not info.context.user.is_authenticated:
            return CreateFilm(form_error=json.dumps("Login required"))
        film = Film(owner=info.context.user, release_date=datetime.datetime.now(), title=title, episode_id=episode_id)
        film.save()
        return CreateFilm(film=film, form_error=None)
