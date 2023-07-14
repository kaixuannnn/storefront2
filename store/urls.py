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

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='products_reviews')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(products_router.urls)),
]
