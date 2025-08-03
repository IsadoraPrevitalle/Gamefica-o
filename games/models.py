from django.db import models
from django.utils import timezone

class Cargo(models.Model):
    time = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField()

    def __str__(self):
        return str(self.nome)

class Usuario(models.Model):
    idcargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')])
    email = models.EmailField()
    senha = models.CharField(max_length=100) #remover

    def __str__(self):
        return str(self.nome)

class Servico(models.Model):
    tipo = models.CharField(choices=[('1', 'SLA'), ('2', 'Desenvolvimento Interno'), ('3', 'Projetos Estruturantes')])
    ponto = models.IntegerField()

    def __str__(self):
        return self.get_tipo_display()

class Criticidade(models.Model):
    tipo = models.CharField(choices=[('1', 'baixa'), ('2', 'normal'), ('3', 'grave'), ('4', 'critica')])
    ponto = models.IntegerField()

    def __str__(self):
        return self.get_tipo_display()
    
class Complexidade(models.Model):
    tipo = models.CharField(choices=[('1', 'C1'), ('2', 'C2'), ('3', 'C3')])
    ponto = models.IntegerField()

    def __str__(self):
        return self.get_tipo_display()

    def __str__(self):
        return str(self.tipo)

class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    idservico = models.ForeignKey(Servico, on_delete=models.PROTECT)
    idcriticidade = models.ForeignKey(Criticidade, on_delete=models.PROTECT)
    idcomplexidade = models.ForeignKey(Complexidade, on_delete=models.PROTECT)
    classe = models.CharField(max_length=100, null=True, blank=True) #deixar classe como charfield
    tempo_estimado = models.FloatField() #tempo em horas?
    tempo_gasto = models.FloatField() #pode ser nulo
    dt_inclusao = models.DateTimeField(default=timezone.now()) 
    dt_entrega = models.DateTimeField(null=True, blank=True)
    dt_encerramento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.nome)[:20] + '...'

class Historico(models.Model):
    idtarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT)
    idusuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    dt_inclusao = models.DateTimeField(auto_now_add=True) 
    finalizada = models.BooleanField()
    pontos = models.IntegerField(null=True, blank= True, default=None)

    #Adiocionar um retorno

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