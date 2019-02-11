from django import forms
from .models import pizza,ingrediente,cliente,orden

class addClienteForm(forms.ModelForm):
    class Meta:
     model=cliente
     fields=['ci','nombre','apellido','telefono']


class ordenPizza(forms.ModelForm):

  def __init__(self, user, *args, **kwargs):
        super(ordenPizza, self).__init__(*args, **kwargs)
        self.fields['fk_cliente'] = forms.ChoiceField(label='Cliente',
            choices=[(o.id, o.nombre) for o in cliente.objects.order_by('nombre','apellido')])
        self.fields['fk_ingrediente'] = forms.ChoiceField(label='Ingrediente',
            choices=[(o.id, o.nombre )for o in ingrediente.objects.order_by('nombre')])
        self.fields['fk_pizza'] = forms.ChoiceField(label='Pizza',
            choices=[(o.id, o.size) for o in pizza.objects.order_by('size')])
       
       

  
  class Meta:
     model=orden
     fields=['fecha','cantidad','total','fk_cliente','fk_ingrediente','fk_pizza']