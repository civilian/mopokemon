from pprint import pprint
from pokemon.models import VisitedEvolutionChains, Pokemon, Species
from consume_rest_service.utils import url_query, get_json_from_url, return_dictionary_from_args

class SaveChainEvolution(object):

    urls_pokeapi = {
        'evolution_chain': "https://pokeapi.co/api/v2/evolution-chain/{chain_id}/"
    }

    def __init__(self, force=False):
        self._force = force
    
    def _continue_saving(self, created):
        """ Method to reduce the complexity of the conditionals
        """
        if self._force:
            return True
        if created:
            return True
        
        return False

    def _save_pokemon_data(self, url_pokemon, species):
        pokemon_json_data = get_json_from_url(url=url_pokemon)
        pokemon = Pokemon()
        try:
            pokemon = Pokemon.objects.get(id=pokemon_json_data['id'])
        except Pokemon.DoesNotExist as e:
            pokemon.id = pokemon_json_data['id']
        pokemon.name = pokemon_json_data['name']
        pokemon.height = pokemon_json_data['height']
        pokemon.weight = pokemon_json_data['weight']
        pokemon.species = species
        for json_stat in pokemon_json_data['stats']:
            setattr(pokemon, json_stat['stat']['name'].replace('-', '_'), json_stat['base_stat'])
        pokemon.save()


    def _save_species_data(self, url_species, pre_evolution_species=None):
        """ Saves the data of the pokemons in one species"""
        species_json_data = get_json_from_url(url=url_species)
        species, created = Species.objects.get_or_create(name=species_json_data['name'], evolves_from=pre_evolution_species)
        for variety in species_json_data['varieties']:
            self._save_pokemon_data(url_pokemon=variety['pokemon']['url'], species=species)
        return species
        

    def _save_all_evolutions(self, evolves_to, pre_evolution_species=None):
        """ Recursively visits the evolutions saving his principal species and then iterating the new evolutions keeping the parent species
        Args: 
            evolves_to list(json(...)): list that contains a main species
        Returns:
            void
        """
        for evolution in evolves_to:
            current_species = self._save_species_data(url_species=evolution['species']['url'], pre_evolution_species=pre_evolution_species)
            self._save_all_evolutions(evolves_to=evolution['evolves_to'], pre_evolution_species=current_species)


    def save_evolution_chain_data(self, chain_id):
        """ Saves all the data of the evolution chain regarding this project
        Args:
            chain_id (int): the id of the chain we are saving
        Returns:
            boolean: wheter or not the evolution chain data has been saved
        """
        visited, created = VisitedEvolutionChains.objects.get_or_create(id=chain_id)
        if not self._continue_saving(created):
            return False

        evolution_chain = get_json_from_url(url=self.urls_pokeapi['evolution_chain'].format(chain_id=chain_id))
        species = self._save_species_data(evolution_chain['chain']['species']['url'])
        self._save_all_evolutions(evolves_to=evolution_chain['chain']['evolves_to'], pre_evolution_species=species)
        
        return True