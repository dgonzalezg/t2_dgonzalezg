from django.urls import path, include
from rest_framework import routers
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
router = routers.DefaultRouter()
#router.register(r'hamburguesa', views.burgers_list)
#router.register(r'ingrediente', views.ingredients_list)
urlpatterns = [
    path('', include(router.urls)),
    path('hamburguesa/', views.burgers_list),
    path('hamburguesa/<pk>', views.burger_detail),
    path('hamburguesa/<int:burguer_id>/ingrediente/<int:ingredient_id>', views.burguer_update),
    path('ingrediente/', views.ingredients_list),
    path('ingrediente/<pk>', views.ingredient_detail, name='ingredient_detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
