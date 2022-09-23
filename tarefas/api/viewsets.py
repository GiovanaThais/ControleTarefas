# from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import filters

from rest_framework import generics

from tarefas.api.serializers import TarefasSerializer, PessoasSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from tarefas import models


class ListarTarefasAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated] #permitindo que view seja autenticada

    serializer_class = TarefasSerializer
    queryset = models.Tarefa.objects.all()

class TarefaAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = models.Tarefa.objects.all()
    serializer_class = TarefasSerializer


class ListarPessoasAPIView(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PessoasSerializer
    queryset = models.Pessoa.objects.all()

class PessoaAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = PessoasSerializer
    queryset = models.Pessoa.objects.all()
