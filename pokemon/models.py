from django.db import models
from django.utils.translation import ugettext_lazy as _

class VisitedEvolutionChains(models.Model):
    """Represents the evolution chains that have been visited and which data has been
    loaded.
    """
    updated_on = models.DateTimeField(auto_now=True, verbose_name=_('updated date'),
        help_text=_('updated date'))

    class Meta:
        verbose_name = _('visited evolution chain')
        verbose_name_plural = _('visited evolution chains')
        ordering = ['id']
    def __str__(self):
        return f"{self.id} {self.updated_on}"

class Species(models.Model):
    """Represents all the data we need for this project conserning the species. """
    name = models.CharField(max_length=50,verbose_name=_('name'), 
        help_text=_('species name'), unique=True)
    evolves_from = models.ForeignKey('Species', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = _('species')
        verbose_name_plural = _('species')
        ordering = ['name']
    def __str__(self):
        return f"{self.id} {self.name}"


class Pokemon(models.Model):
    """Represents all the data we need for this project conserning the pokemon. """
    name = models.CharField(max_length=50,verbose_name=_('name'), 
        help_text=_('pokemon name') )
    height = models.IntegerField(verbose_name=_('height'), help_text=_('height'))
    weight = models.IntegerField(verbose_name=_('weight'), help_text=_('weight'))
    hp = models.IntegerField(verbose_name=_('hp'), help_text=_('hp'))
    attack = models.IntegerField(verbose_name=_('attack'), help_text=_('attack'))
    defense = models.IntegerField(verbose_name=_('defense'), help_text=_('defense'))
    special_attack = models.IntegerField(verbose_name=_('special attack'), 
        help_text=_('special attack'))
    special_defense = models.IntegerField(verbose_name=_('special defense'), 
        help_text=_('special defense'))
    speed = models.IntegerField(verbose_name=_('speed'), help_text=_('speed'))
    species = models.ForeignKey('Species', on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('pokemon')
        verbose_name_plural = _('pokemons')
        ordering = ['id']
        # and index is not necesary there are a small number of pokemons
        # rounding in the thousands https://www.cbr.com/pokemon-questions-answers-facts-trivia/
        # indexes = [
        #     models.Index(fields=['id'], name='pokemon_idx'),
        # ]

    def __str__(self):
        return f"{self.id} {self.name}"