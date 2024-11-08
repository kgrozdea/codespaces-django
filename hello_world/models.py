from django.db import models
from django.utils import timezone

class materia(models.Model):
    id = models.IntegerField()
    nome = models.CharField(max_lenght = 15)
    professores = models.ManyToManyField(professor,  related_name="alunos")
    def __str__(self):
        return self.nome


class professor(models.Model):
    matricula = models.IntegerField()
    nomeProf = models.CharField(max_lenght = 100)
    email = models.EmailField()
    telefone = models.IntegerField
    def __str__(self):
        return self.nomeProf

class turma(models.Model):
    codigo = models.IntegerField()
    materia = models.IntegerChoices(choices = materia)
    nome = models.ForeignKey(professor, on_delete=models.CASCADE)
    def __str__(self):
        return "%d%d" % (self.materia, self.codigo)
    

class aluno(models.Model):
    matricula = models.IntegerField()
    nomeAluno =  models.CharField(max_lenght = 100)
    email = models.EmailField()
    turmas = models.ManyToManyField(turma,  related_name="alunos")
    def __str__(self):
        return self.nomeAluno
    

class coordenador(models.Model):
    matricula = models.IntegerField()
    nomeCoord = models.CharField(max_lenght = 100)
    email = models.EmailField()
    telefone = models.IntegerField
    def __str__(self):
        return self.nomeCoord
    
class aviso(models.Model):
    id = models.IntegerField()
    titulo = models.CharField(max_lenght = 100)
    def __str__(self):
        return self.titulo
    descricao = models.TextField()
    data = models.DateTimeField(default=timezone.now)
