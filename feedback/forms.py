from django import forms
from .models import Feedback

class FeedbackCreateForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['nombre', 'apellido', 'email', 'direccion',
        'codigo_postal', 'mensaje']