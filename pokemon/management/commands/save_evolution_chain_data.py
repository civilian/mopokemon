from django.core.management.base import BaseCommand, CommandError
from ._private_save_evolution_chain import SaveChainEvolution

class Command(BaseCommand):
    help = 'Saves data of the pokemons that are present in a evolution chain of https://pokeapi.co/'

    def add_arguments(self, parser):
        """Adds the arguments that are acepted in the command."""
        parser.add_argument('chain_id', type=int, help='the id of the evolution chain')
        parser.add_argument('--force', action='store_true',
            help='Force the algorithm to save the data even if it already exists',)

    def handle(self, *args, **options):
        """Runs the command."""
        chain_id = options['chain_id']
        force = options['force']
        save_evolution_chain = SaveChainEvolution(force)
        if save_evolution_chain.save_evolution_chain_data(chain_id):
            self.stdout.write(self.style.SUCCESS(f'Successfully saved the data of the evolution chain {chain_id}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Evolution chain {chain_id} already saved'))
