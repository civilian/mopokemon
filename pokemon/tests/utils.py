from io import StringIO
from django.core.management import call_command

def call_command_save_evolution_chain_data(*args, **kwargs):
    out = StringIO()
    call_command(
        "save_evolution_chain_data",
        *args,
        stdout=out,
        stderr=StringIO(),
        **kwargs,
    )
    return out.getvalue()

ivysaur_data = {
            "id": 2,
            "name": "ivysaur",
            "height": 10,
            "weight": 130,
            "hp": 60,
            "attack": 62,
            "defense": 63,
            "special_attack": 80,
            "special_defense": 80,
            "speed": 60,
            "evolutions": [
                {
                    "id": 3,
                    "name": "venusaur"
                },
                {
                    "id": 10033,
                    "name": "venusaur-mega"
                },
                {
                    "id": 10186,
                    "name": "venusaur-gmax"
                }
            ],
            "pre_evolutions": [
                {
                    "id": 1,
                    "name": "bulbasaur"
                }
            ]
        }