
from importlib import import_module
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from crudapp.forms import UserForm
from django.http import HttpResponse
from crudapp.models import User

# Create your views here.

def insert(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        verify = request.POST
        for key,value in verify.items():
            if key == 'uname':
                print(value)
        if form.is_valid:
            try:
                form.save()
                return HttpResponse("Data sent ro database successfully......")
            except:
                pass 
        
    form = UserForm()

    return render(request, 'index.html', {'form':form})


def show(request):
    users =     User.objects.all()

    # for user in users:
    #     print(user.id)
     
    return render(request,'show.html',{'users':users})


def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()

    return redirect('/show')



def edit(request,id):
    user = User.objects.get(id=id)
    return render(request,'edit.html',{'user':user})


def update(request,id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST,instance=user)
    if form.is_valid():
        form.save()
        print('enter')
        return redirect('/show')
        
    print('dont enter')
    return render(request,'edit.html',{'user':user })

