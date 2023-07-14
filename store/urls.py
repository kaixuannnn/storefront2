from django.urls import include, path
from rest_framework.routers import SimpleRouter
from . import views
from pprint import pprint

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
pprint(router.urls)

urlpatterns = [
     path('', include(router.urls))
]
