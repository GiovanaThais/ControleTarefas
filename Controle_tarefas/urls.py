from django.contrib import admin
from django.urls import path, include

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from tarefas.api.viewsets import ListarTarefasAPIView, TarefaAPIView, ListarPessoasAPIView, PessoaAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("tarefas/", include("tarefas.urls")),
    
    #rotas da api rest 
    path('api/', ListarTarefasAPIView.as_view(), name='tarefas_api'),
    path('api/<int:pk>/', TarefaAPIView.as_view(), name='tarefa_api'),
    path('api/pessoas/', ListarPessoasAPIView.as_view(), name='pessoas_api'),
    path('api/pessoas/<int:pk>/', PessoaAPIView.as_view(), name='pessoa_api'),
]
