from django.contrib import admin
from .models import materia, professor, turma, aluno, coordenador, aviso

class ReferenciaAdmin (admin.ModelAdmin):
    list_display = ['materia', 'professor', 'turma', 'aluno', 'coordenador', 'aviso']

admin.site.register(Referencia, ReferenciaAdmin)
