from django.forms import forms, ModelForm, TextInput, Textarea
from .models import Contacto

from .models import Contacto


class ContactForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        exclude = ['created_at',]
        widgets = {
            'message': Textarea,
        }
        labels = {
            'name': 'Nombre',
            'subject': 'Asunto',
            'email':'Correo',
            'message':'Mensaje',
        }
