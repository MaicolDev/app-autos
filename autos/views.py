from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import FormularioAuto
from .models import Auto

# Create your views here.



def registro(request):
    if request.method == "GET":
        return render(request, "registrarse.html",{
            "form" : UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("inicio")
            except IntegrityError:
                return render(request, "registrarse.html",{
                "form" : UserCreationForm, "error": "el usuario ya existe"
        })

        else:
            return render(request, "registrarse.html",{
                "form" : UserCreationForm, "error": "las contraseñas no coinciden"
        })


def inicio(request):
    autos= Auto.objects.filter(vendido=False).order_by("-fecha")
    return render(request,"inicio.html",{
        'autos':autos
    })

def autos(request):
    autos = Auto.objects.filter(propietario=request.user, vendido__isnull=False).order_by("-fecha")
    return render(request,"autos.html",{
        'autos':autos
    })

def auto_detalle(request, auto_id):
    auto =get_object_or_404(Auto ,pk=auto_id)
    return render(request,'auto_detalle.html',{
        'auto':auto
    })

def auto_editar(request, auto_id):
    if request.method == "GET":
        auto = get_object_or_404(Auto,pk=auto_id)
        formulario= FormularioAuto(instance=auto)
        return render(request,"auto_editar.html",{"formulario": formulario})

    else:
        auto = get_object_or_404(Auto,pk=auto_id)
        form = FormularioAuto(request.POST, instance=auto)
        form.save()
        return redirect('autos')


    



def cerrar_sesion(request):
    logout(request)
    return redirect("registro")


def iniciar_sesion(request):
    if request.method == "GET":
        return render(request, "iniciarsesion.html",{
        "form": AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, "iniciarsesion.html",{
            "form": AuthenticationForm, "error":"el usuario o la contraseña estan mal"
            })

        else:
            login(request,user)
            return redirect("inicio")

       

def crear_auto(request):

    if request.method =='GET':
        return render(request, 'nuevo_auto.html',{
        "form":FormularioAuto
    })
    else:
        try:
            form = FormularioAuto(request.POST)
            nuevo_auto= form.save(commit=False)
            nuevo_auto.propietario = request.user
            nuevo_auto.save()
            return redirect('inicio')
        except ValueError:
            return render(request, 'nuevo_auto.html',{
            "form":FormularioAuto, "error":"provee datos validos"
            })
        
    


