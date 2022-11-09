from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AreaView, ConsultorioView, PesquisadoView, PesquisaView

router = SimpleRouter()
router.register('area', AreaView, basename='area')
router.register('consultorio', ConsultorioView, basename='consultorio')
router.register('pesquisado', PesquisadoView, basename='pesquisado')
router.register('pesquisa', PesquisaView, basename='pesquisa')

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
] + router.urls
