from rest_framework.serializers import ModelSerializer
from core.models import PontosTuristicos


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontosTuristicos
        fields = ('id', 'nome', 'descricao')
