from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from .models import Food, FoodCategory, FoodSerializer, FoodListSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )
        return queryset


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(is_publish=True).select_related()
    serializer_class = FoodSerializer


def index(request):
    return HttpResponse("HELLOY")
