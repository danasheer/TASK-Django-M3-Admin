from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = 'WA', _('Water')
        GRASS = 'GR', _('Grass')
        GHOST = 'GH', _('Ghost')
        STEEL = 'ST', _('Steel')
        FAIRY = 'FA', _('Fairy')
    name = models.CharField(max_length=30)
    type = models.CharField(
        max_length=2,
        choices=PokemonType.choices
    )
    hp = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30, default="",blank=True)
    name_ar = models.CharField(max_length=30, default="",blank=True)
    name_jp = models.CharField(max_length=30, default="",blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
