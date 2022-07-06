from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion',
                  'codigo_postal', 'ciudad']