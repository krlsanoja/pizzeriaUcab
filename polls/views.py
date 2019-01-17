
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from.models import pizza,ingrediente
from .forms  import addClienteForm,ordenPizza

# Create your views here.

def index(request):
    
     return render(request,'polls/home.html')



def order(request):
   
   form=addClienteForm(request.POST or None)
   if request.method == 'POST':
       form=addClienteForm(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponseRedirect('/compra/')
       else:
          form=addClienteForm()    
      
   return render(request,'polls/orden.html',{'form':form})

def orders(request):
  
   form=ordenPizza(request.POST or None)
   if request.method == 'POST':
       form=ordenPizza(request.POST)
       if form.is_valid():
          form.save()
          return HttpResponse('Gracias por su orden')  
       else:
          form=ordenPizza()   
      
   return render(request,'polls/compra.html',{'form':form})
