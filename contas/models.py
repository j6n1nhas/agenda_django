from django.db import models
from contactos.models import Contacto
from django import forms


# Create your models here.
class FormContacto(forms.ModelForm):
    """
    ModelForm criado a partir do model Contacto. Neste caso é para ser utilizado como uma form na dashboard do utilizador
    para que ele possa inserir um contacto na base de dados. Muito facilmente conseguimos criar uma form a partir de um
    model, e neste caso não escluímos campo nenhum, portanto todos os campos vão estar presentes na form quando a
    enviarmos par a página html.
    """
    class Meta:
        model = Contacto
        exclude = ()