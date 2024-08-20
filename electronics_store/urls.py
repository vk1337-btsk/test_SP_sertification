from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import ElectronicsStoreConfig
from .views import NetworkNodeViewSet, ProductViewSet


app_name = ElectronicsStoreConfig.name


router = DefaultRouter()
router.register(r"network_nodes", NetworkNodeViewSet)
router.register(r"products", ProductViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
]
