from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontosTuristicos.objects.all()
    serializer_class = PontoTuristicoSerializer
