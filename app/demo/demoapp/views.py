from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from demoapp.models import Dog, Cat
from demoapp.serializers import CatSerializer, DogSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Cat"])
class CatViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "breed", "age", "sex", "adopted", "weight"]
    