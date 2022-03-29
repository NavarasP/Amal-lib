from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponseRedirect
from questionpool.forms import Qform

from questionpool.models import *

# from questionpool.models import question

# Create your views here.



class Questionpool(View):
    def get(self,request):
        return render(request,"questionpool.html")


def Adminquestion(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if user.is_superuser:
            quesad=quesadmin.objects.all()
            return render(request,"adminques.html",
                          {
                              'quesad':quesad
                          })
            
        else:
            return redirect('/')
            #u r notan admin "Alert"
    
    else:
        return redirect('/')


        #u r not logged in "Alert"

def Addquestion(request):
    if request.user.is_authenticated:
        user=User.objects.get(pk=request.user.id)
        if quesadmin.objects.filter(quesadmin_username=user).exists():
            if request.method == 'POST':
                form=Qform(request.POST, request.FILES)
                newques = form.save(commit=False)
                newques.save()
                return redirect('Addquestion')
            else:
                postques=Qform()
                dept=department.objects.all()
                subj=subject.objects.all()
                return render(request, 'addquestion.html', {
                    'postques': postques,
                    'dept':dept,
                    'subj':subj,
                })



        else:
            return redirect('/')
            #u r not an admin "Alert"
    else:
        return redirect('/')
        #u r not logged in "Alert"