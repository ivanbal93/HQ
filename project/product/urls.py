from rest_framework.routers import SimpleRouter

from .views import ProductViewSet

router = SimpleRouter()

router.register('api/product', ProductViewSet)
