from django.db import models


class Pessoa(models.Model):
    nome = models.CharField("nome", max_length=150)
    email = models.EmailField("email", blank=False, null=True)
    telefone = models.CharField("telefone", max_length=12, blank=False, null=True)

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        db_table= 'pessoa'
        verbose_name = "Pessoa" 
        verbose_name_plural = "Pessoas"


class Tarefa(models.Model):

    OPCOES_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado'),
    )
    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'), 
        ('precisa ser feito', 'Precisa ser feito'),
    )
    OPCOES_COMPLEXIDADE = (
        ('muito fácil', 'Muito fácil'),
        ('fácil', 'Fácil'),
        ('regular', 'Regular'),
        ('complexo', 'Complexo'),
        ('muito complexo', 'Muito complexo'),
    )
    descricao = models.CharField("descrição", max_length=400)
    criacao = models.DateField("criacao", auto_now_add=True)
    categoria = models.CharField("categoria", max_length=25,
                                 choices=OPCOES_CATEGORIA,
                                 default='importante')
    status = models.CharField("status", max_length=25, choices=OPCOES_STATUS,
                             default='pendente')
    data_entrega = models.DateField("data_entrega", auto_now_add=False, blank=False, null=True, default=None)
    complexidade = models.CharField("complexidade", max_length=25, blank=True, null=True,
                                    choices=OPCOES_COMPLEXIDADE)
    pessoas = models.ManyToManyField(Pessoa)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table= 'tarefa'
        verbose_name = "Tarefa" 
        verbose_name_plural = "Tarefas"
