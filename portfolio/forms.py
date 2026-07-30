from django import forms

from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ["nombre", "email", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "mt-1 w-full px-4 py-2 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-colors",
                    "placeholder": "Juan Pérez",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "mt-1 w-full px-4 py-2 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-colors",
                    "placeholder": "juan@empresa.com",
                }
            ),
            "mensaje": forms.Textarea(
                attrs={
                    "rows": 4,
                    "class": "mt-1 w-full px-4 py-2 bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-100 border border-slate-300 dark:border-slate-700 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none transition-colors",
                    "placeholder": "Cuéntame sobre tu proyecto...",
                }
            ),
        }
