
from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  #this is calculator  
#def operations(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # add=x+y
    #sub=x-y
   # mul=x*y
    #div=x/y
    #mod=x%y
   # return render(request,"result.html",{'fnum':x,'snum':y,'addition':add,'substraction':sub,'multiplication':mul,'division':div,'modulus':mod,})
