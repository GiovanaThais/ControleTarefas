from .models import Tarefa, Pessoa
from django import forms


class AdicionarPessoas(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'telefone')

class EditarPessoasForm(forms.Form):
    
    nome = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefone = forms.CharField(max_length=14)

class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'categoria', 'complexidade', 'data_entrega', 'pessoas')
    

class EditarTarefaForm(forms.Form):
    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito')
    )
    OPCOES_COMPLEXIDADE = (
        ('muito fácil', 'Muito fácil'),
        ('fácil', 'Fácil'),
        ('regular', 'Regular'),
        ('complexo', 'Complexo'),
        ('muito complexo', 'Muito complexo'),
    )
    tarefa = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(choices=OPCOES_CATEGORIA)
    complexidade = forms.ChoiceField(choices=OPCOES_COMPLEXIDADE)
    data_entrega = forms.DateField()  #formato igual a: aaaa/mm/dd
    pessoas = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Pessoa.objects.all()
               )
