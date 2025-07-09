# usually stays in urls.py

from rest_framework.routers import DefaultRouter
from products.viewsets import ProductGenericViewSet

router = DefaultRouter()
router.register("products-list", ProductGenericViewSet, basename="products")

urlpatterns = router.urls