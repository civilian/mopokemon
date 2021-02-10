from io import StringIO
from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from rest_framework.test import APIClient
from pokemon.tests.utils import call_command_save_evolution_chain_data, ivysaur_data

class PokemonApiTests(TestCase):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = APIClient()
    
    def _get_api(self, url='/api/v1/pokemon/', pokemon='ivysaur'):
        return self.client.get(url+str(pokemon)+"/")

    def test_api_failure(self):
        ans = self._get_api()
        self.assertEqual(ans.status_code, 404)
        wrong_pokemon = 'That pokemon name is not found, maybe you need to run the command [$ docker-compose run rest-service python ' \
                        'manage.py save_evolution_chain_data CHAIN_ID] with another evolution chain'
        self.assertEqual(ans.data['detail'], wrong_pokemon)

    def test_api_success(self):
        chain_id = 1
        out = call_command_save_evolution_chain_data(chain_id)
        ans = self._get_api()
        self.assertEqual(ans.status_code, 200)
        self.assertEqual(ans.data, ivysaur_data)
    
    def test_api_failure_not_a_pokemon(self):
        ans = self._get_api(pokemon=2)
        self.assertEqual(ans.status_code, 404)
        wrong_pokemon = 'That pokemon name is not found, maybe you need to run the command [$ docker-compose run rest-service python ' \
                        'manage.py save_evolution_chain_data CHAIN_ID] with another evolution chain'
        self.assertEqual(ans.data['detail'], wrong_pokemon)
    