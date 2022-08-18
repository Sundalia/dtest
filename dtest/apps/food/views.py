from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from .models import Food, FoodCategory, FoodSerializer, FoodListSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.prefetch_related(
            Prefetch('food', queryset=Food.objects.filter(is_publish=True))
        )
        return queryset


def index(request):
    return HttpResponse("HELLOY")
