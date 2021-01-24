from rest_framework import serializers

from pokemon.models import Pokemon

class PokemonMiniSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ['id', 'name']

class PokemonSerializer(serializers.ModelSerializer):

    pre_evolutions = serializers.SerializerMethodField(read_only=True, required=False)
    evolutions = serializers.SerializerMethodField(read_only=True, required=False)

    def get_pre_evolutions(self, obj):
        try:
            return PokemonMiniSerializer(obj.species.evolves_from.pokemon_set, read_only=True, many=True, required=False).data
        except AttributeError as e:
            return []
    
    def get_evolutions(self, obj):
        try:
            evolutions = []
            # Choosed the for because the map is not readable
            for species in obj.species.species_set.all():
                evolutions.extend(species.pokemon_set.all())
            return PokemonMiniSerializer(evolutions, read_only=True, many=True, required=False).data
        except AttributeError as e:
            print(e)
            return []

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'evolutions', 'pre_evolutions']