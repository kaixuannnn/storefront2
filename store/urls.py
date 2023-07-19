from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views
from pprint import pprint
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('carts',views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router,'carts',lookup='cart' )
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
    path(r'', include(carts_router.urls))
]
