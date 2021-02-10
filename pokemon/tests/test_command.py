from django.core.management.base import CommandError
from django.test import TestCase
from pokemon.tests.utils import call_command_save_evolution_chain_data
from pokemon.models import Pokemon, Species, VisitedEvolutionChains

class SaveEvolutionChainDataCommandIntegrationTests(TestCase):

    def test_command_fails_whitout_args(self):
        with self.assertRaises(CommandError):
            call_command_save_evolution_chain_data()
    
    def test_command_success(self):
        chain_id = 1
        out = call_command_save_evolution_chain_data(chain_id)
        self.assertEqual(out, f'\x1b[32;1mSuccessfully saved the data of the evolution chain {chain_id}\x1b[0m\n')
        self.assertEqual(Pokemon.objects.count(), 5)
        self.assertEqual(Species.objects.count(), 3)
        self.assertEqual(VisitedEvolutionChains.objects.count(), 1)
    
    def test_command_repeat_the_save(self):
        chain_id = 1
        out = call_command_save_evolution_chain_data(chain_id)
        out = call_command_save_evolution_chain_data(chain_id)
        self.assertEqual(out, f'\x1b[32;1mEvolution chain {chain_id} already saved\x1b[0m\n')
    
    def test_command_success_twice(self):
        chain_id = 1
        out = call_command_save_evolution_chain_data(chain_id)
        chain_id_second = 2
        out = call_command_save_evolution_chain_data(chain_id_second)
        self.assertEqual(out, f'\x1b[32;1mSuccessfully saved the data of the evolution chain {chain_id_second}\x1b[0m\n')
        self.assertEqual(Pokemon.objects.count(), 11)
        self.assertEqual(Species.objects.count(), 6)
        self.assertEqual(VisitedEvolutionChains.objects.count(), 2)