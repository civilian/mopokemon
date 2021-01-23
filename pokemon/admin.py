from django.contrib import admin
from .models import Pokemon, Species, VisitedEvolutionChains

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass

@admin.register(VisitedEvolutionChains)
class VisitedEvolutionChainsAdmin(admin.ModelAdmin):
    pass
