from django.shortcuts import render
from django.views import View
from.forms import RegForm
from.models import Reg
from django.http import HttpResponse
class RegInput(View):
    def get(self,request):
        rf=RegForm()
        con_dict={"regform":rf}
        return render(request,'reginput.html',con_dict)
def valid():
    pass
class Register(View):
    def post(self,request):
     rf=RegForm(request.POST)
     if rf is valid():
      rf.save()
      return HttpResponse("successfully registered")
