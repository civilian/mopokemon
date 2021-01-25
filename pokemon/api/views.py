from django.http import Http404

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from pokemon.models import Pokemon
from .serializers import PokemonSerializer

class PokemonRetrieveViewSet(mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    lookup_field = 'name'

    def handle_exception(self, exc):
        """"Custom handler of NOT-FOUND exception to properly inform the user"""
        if isinstance(exc, Http404):
            return Response({'detail': 'That pokemon name is not found, '
                            'maybe you need to run the command [$ docker-compose run rest-service python manage.py save_evolution_chain_data CHAIN_ID] '
                            'with another evolution chain'}, 
                            status=status.HTTP_404_NOT_FOUND)

        return super().handle_exception(exc)