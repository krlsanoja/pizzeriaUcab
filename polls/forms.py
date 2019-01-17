from django import forms
from .models import pizza,ingrediente,cliente,orden

class addClienteForm(forms.ModelForm):
    class Meta:
     model=cliente
     fields=['ci','nombre','apellido','telefono']


class ordenPizza(forms.ModelForm):

  fecha=forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker'
                                })) 
  client = [(c.id, c.nombre) for c in cliente.objects.all()]
  pizza_choices = [(p.id, p.size) for p in pizza.objects.all()]
  ingrediente_choices = [(i.id, i.nombre) for i in ingrediente.objects.all()]
  fk_cliente=forms.ChoiceField(required=True, label='Cliente', choices=client)
  fk_pizza = forms.ChoiceField(required=True, label='Pizza', choices=pizza_choices)
  fk_ingrediente = forms.ChoiceField(required=True, label='Ingredientes',widget=forms.Select,choices=ingrediente_choices)

  class Meta:
     model=orden
     fields=['fecha','cantidad','total','fk_cliente','fk_ingrediente','fk_pizza']