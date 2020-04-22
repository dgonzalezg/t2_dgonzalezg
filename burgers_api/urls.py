from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'hamburguesa', views.HamburguesaViewSet)
router.register(r'ingrediente', views.IngredientesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hamburguesa/<int:id>/ingrediente/<int:id>/', views.HamburguesaViewSet, views.IngredientesViewSet),
]