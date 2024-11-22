from django import forms
from .models import aviso

class adicionaAviso(forms.ModelForm):
    class Meta:
        model = aviso
        fields = ['titulo', 'descricao']
