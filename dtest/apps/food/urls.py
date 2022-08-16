from django.urls import path, include
from rest_framework import routers
from .views import FoodViewSet, FoodCategoryViewSet
from . import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'food', FoodCategoryViewSet, basename='food')
urlpatterns = [
    path('', views.index, name='index'),
    path('v1/', include(router_v1.urls))
]