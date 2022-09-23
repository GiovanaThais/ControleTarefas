from django.contrib import admin
from .models import Tarefa, Pessoa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("descricao", "categoria", "criacao",
         "status", "data_entrega", "complexidade")
    list_editable = ("data_entrega", "complexidade")
    list_filter = ("categoria", "status")
    search_fields = [ "descricao","categoria","status",]

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone")
