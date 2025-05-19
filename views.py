from django.shortcuts import render
from .forms import Eoform
def home(request):
    if request.GET.get("num"):
        num=float(request.GET.get("num"))
        res="Even number " if num%2==0 else "Odd number"
        msg="ur number "+str(num)+" is "+str(res)
        fm=Eoform()
        return render(request,"home.html",{"fm":fm,"msg":msg})
    else:
        fm=Eoform()
        return render(request,"home.html",{"fm":fm})
# Create your views here.
