from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from crypto.viewsets import CryptocurrencyViewSet
from forex.viewsets import CurrencyViewSet
from market.viewsets import StockViewSet
from users.viewsets import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("User", UserViewSet)
router.register("Stocks", StockViewSet)
router.register("Currency", CurrencyViewSet)
router.register("Cryptocurrency", CryptocurrencyViewSet)

app_name = "api"
urlpatterns = router.urls
