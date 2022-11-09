from rest_framework.serializers import ModelSerializer
from .models import Area, Consultorio, Pesquisado, Pesquisa


class AreaSerializer(ModelSerializer):
    class Meta:
        fields = ('nombre', 'municipio', 'provincia',)
        model = Area


class ConsultorioSerializer(ModelSerializer):
    class Meta:
        fields = ('numero', 'direccion', 'nombreArea',)
        model = Consultorio


class PesquisadoSerializer(ModelSerializer):
    class Meta:
        fields = ('CI', 'nombre', 'primerApellido',
                  'segundoApellido', 'numero',)
        model = Pesquisado


class PesquisaSerializer(ModelSerializer):
    class Meta:
        fields = ('id','CI', 'fecha', 'encamado', 'contacto', 'familiaRiesgo',)
        model = Pesquisa
