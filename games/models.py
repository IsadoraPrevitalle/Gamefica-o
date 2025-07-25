from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Cargo(models.Model):
    time = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField()

    def __str__(self):
        return str(self.time)

class Usuario(models.Model):
    idcargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(60)])
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminio'), ('O', 'Outros')])
    email = models.EmailField()
    senha = models.CharField(max_length=100)

    def __str__(self):
        return str(self.nome)

class Servico(models.Model):
    tipo = models.CharField(choices=[('1', 'SLA'), ('2', 'Desenvolvimento Interno'), ('3', 'Projetos Estruturantes')])
    ponto = models.IntegerField()

    def __str__(self):
        return str(self.tipo)

class Criticidade(models.Model):
    tipo = models.CharField(choices=[('1', 'baixa'), ('2', 'normal'), ('3', 'grave'), ('4', 'critica')])
    ponto = models.IntegerField()

    def __str__(self):
        return str(self.tipo)
    
class Complexidade(models.Model):
    tipo = models.CharField(choices=[('1', 'C1'), ('2', 'C2'), ('3', 'C3')])
    ponto = models.IntegerField()

    def __str__(self):
        return str(self.tipo)

class Classe(models.Model):
    tipo = models.CharField(max_length=50)
    ponto = models.IntegerField()

    def __str__(self):
        return str(self.tipo)

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    idservico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    idcriticidade = models.ForeignKey(Criticidade, on_delete=models.PROTECT)
    idcomplexidade = models.ForeignKey(Complexidade, on_delete=models.PROTECT)
    idclasse = models.ForeignKey(Classe, on_delete=models.PROTECT)
    tempo_estimado = models.FloatField()
    tempo_gasto = models.FloatField()
    dt_inclusao = models.DateTimeField(default=timezone.now()) 
    dt_entrega = models.DateTimeField(null=True, blank=True)
    dt_encerramento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.nome)[:20] + '...' #VERIFICAR NA VIDEO AULA O PQ DO ERRO

class Historico(models.Model):
    idtarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT)
    idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True) 
    finalizada = models.BooleanField()
    pontos = models.IntegerField(null=True, blank= True, default=None)

class Recompensa(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.URLField()
    descricao = models.TextField()
    total_pontos = models.IntegerField()
    idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    idhistorico = models.ForeignKey(Historico, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.nome)