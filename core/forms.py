from django import forms
from django.contrib.auth.models import User
from .models import Perfil

# Formulario para editar datos básicos (Usuario, Email, Nombre)
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        help_texts = {
            'email': None, # Para quitar textos de ayuda molestos
        }

# Formulario para editar datos extra (Avatar, Bio, Web)
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'link']