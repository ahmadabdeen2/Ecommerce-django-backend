from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import ProductViewSet, RatingViewSet, OrderViewSet, OrderItemViewSet

router.register(r'products', ProductViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'orderitems', OrderItemViewSet, basename='orderitems')

urlpatterns = router.urls
