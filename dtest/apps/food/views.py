from django.http import HttpResponse
from rest_framework import viewsets
from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from .models import Food, FoodCategory, FoodSerializer, FoodListSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = FoodListSerializer
    queryset = FoodCategory.objects.prefetch_related(Prefetch('food', queryset=Food.objects.filter(is_publish=True))


def index(request):
    return HttpResponse("HELLOY")
