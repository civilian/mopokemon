from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import PokemonRetrieveViewSet

app_name = "api_pokemon"

router = DefaultRouter()
router.register(r'pokemon', PokemonRetrieveViewSet, basename='pokemon')
urlpatterns = router.urls