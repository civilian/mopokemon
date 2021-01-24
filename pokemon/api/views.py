from rest_framework import mixins, viewsets

from pokemon.models import Pokemon
from .serializers import PokemonSerializer

class PokemonRetrieveViewSet(mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
    lookup_field = 'name'