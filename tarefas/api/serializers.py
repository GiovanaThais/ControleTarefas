from rest_framework import serializers
from tarefas import models


#serializando dados do model
class TarefasSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Tarefa
        fields= '__all__'

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Pessoa
        fields= '__all__'
