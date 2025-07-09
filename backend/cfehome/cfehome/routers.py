# usually stays in urls.py

from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet

router = DefaultRouter()
router.register("products-list", ProductViewSet, basename="products")

urlpatterns = router.urls