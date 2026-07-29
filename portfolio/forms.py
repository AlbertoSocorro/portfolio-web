from django import forms

from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ["nombre", "email", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "mt-1 w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none",
                    "placeholder": "Juan Pérez",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "mt-1 w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none",
                    "placeholder": "juan@empresa.com",
                }
            ),
            "mensaje": forms.Textarea(
                attrs={
                    "rows": 4,
                    "class": "mt-1 w-full px-4 py-2 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none",
                    "placeholder": "Cuéntame sobre tu proyecto...",
                }
            ),
        }
