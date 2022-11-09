from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Area, Consultorio, Pesquisado, Pesquisa
from .serializers import AreaSerializer, ConsultorioSerializer, PesquisadoSerializer, PesquisaSerializer


class AreaView(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class ConsultorioView(ModelViewSet):
    queryset = Consultorio.objects.all()
    serializer_class = ConsultorioSerializer


class PesquisadoView(ModelViewSet):
    queryset = Pesquisado.objects.all()
    serializer_class = PesquisadoSerializer


class PesquisaView(ModelViewSet):
    queryset = Pesquisa.objects.all()
    serializer_class = PesquisaSerializer
