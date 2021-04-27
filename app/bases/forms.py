from django import forms
from django.forms import ModelForm
from .models import Contacto

# class ProductoForm(ModelForm):
    
    # class Meta:
    #     model= Producto
    #     fields=['codigo','nombre', 'marca','descripcion','precio','categoria','emprendimiento','imagen']
    #     o podemos poner de la siguiente manera, asi referenciamos a todos y no a uno por uno como en el caso anterior.
    #     fields='__all__'
        
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model=Contacto
        fields=["nombre", "email", "telefono", "mensaje"]
        