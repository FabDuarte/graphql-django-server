from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('api/auth/', include('rest_framework.urls')),
    path('api/token/auth', obtain_jwt_token),
    path('api/token/refresh', refresh_jwt_token)
]
