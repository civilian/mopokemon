from pprint import pprint
from pokemon.models import VisitedEvolutionChains, Pokemon, Species
from consume_rest_service.utils import get_json_from_url, return_dictionary_from_args

class SaveChainEvolution(object):

    urls_pokeapi = {
        'evolution_chain': "https://pokeapi.co/api/v2/evolution-chain/{chain_id}/"
    }

    def __init__(self, force=False):
        """Initiates the SaveChainEvolution method
        Args:
            force boolean: are you forcing the Chain to be saved?
        Returns:
            SaveChainEvolution object
        """
        self._force = force
    
    def _continue_saving(self, created):
        """ Method to reduce the complexity of the conditionals, returns true if we can keep saving the data of this evolution chain
        Args:
            created boolean: if the VisitedEvolutionChains is new or not
        Returns:
            boolean
        """
        # If you are forcing this evolution chain to be saved
        if self._force:
            return True
        if created:
            return True
        
        return False

    def _save_pokemon_data(self, url_pokemon, species):
        """ Saves the data of one pokemons
        Args:
            url_pokemon str: url of pokeapi regarding a pokemon
            species object models.Species: the species of this pokemon
        Returns:
            void
        """
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
        print(f"{pokemon} saved")


    def _save_species_data(self, url_species, pre_evolution_species=None):
        """ Saves the data of the pokemons in one species
        Args:
            url_species str: url of pokeapi regarding an species
            pre_evolution_species object models.Species: the species of the preevoution of the species we are saving
        Returns:
            void
        """
        
        species_json_data = get_json_from_url(url=url_species)
        species, created = Species.objects.get_or_create(name=species_json_data['name'], evolves_from=pre_evolution_species)
        for variety in species_json_data['varieties']:
            self._save_pokemon_data(url_pokemon=variety['pokemon']['url'], species=species)
        return species
        

    def _save_all_evolutions(self, evolves_to, pre_evolution_species=None):
        """ Recursively visits the evolutions saving his principal species and then iterating the new evolutions keeping the parent species
        Args: 
            evolves_to list(json(...)): list that contains a main species and recursively a list with his same structure(comes from the api)
            pre_evolution_species object models.Species: the species of the preevoution of the species we are saving
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