from email.mime import image
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import User_registration_form, Formulario_profile, Formulario_profileImage
from django.contrib.auth.decorators import login_required
from users.models import User_profile



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                try:
                    if request.user.profile.user_id == request.user.id:
                        pass
                except:
                    User_profile.objects.create(user_id = request.user.id)
                context = {'user':f'{username}'}
                return redirect('inicio')

        form = AuthenticationForm()
        return render(request, 'users/login.html', {'error': 'Formulário inválido', 'form': form})

    elif request.method == 'GET':
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login_request')
        else:
            context = {'errors':form.errors}
            form = User_registration_form()
            context['form'] = form
            return render(request, 'users/register.html', context)

    elif request.method == 'GET':
        form = User_registration_form()
        return render(request, 'users/register.html', {'form': form})

@login_required
def EditarPerfil(request):
        if request.method == 'POST':
            form = Formulario_profile(request.POST, request.FILES)

            if form.is_valid():
                request.user.profile.phone = form.cleaned_data['phone']
                request.user.profile.address = form.cleaned_data['address']
                request.user.profile.save()
                if request.user.profile.phone and request.user.profile.address:
                    request.user.profile.is_active = True
                    request.user.profile.save()
                else:
                    request.user.profile.is_active = False
                    request.user.profile.save()
                return redirect(Perfil)
        elif request.method == 'GET':
            if request.user.profile.image:
                image = request.user.profile.image
            else:
                image = ''
            form = Formulario_profile(initial={'phone': request.user.profile.phone,
            'address': request.user.profile.address, 
            'image': image  })
            context = {'form': form}
            return render(request, 'users/profileEditar.html', context=context)

@login_required
def EditarPerfilImage(request):
        if request.method == 'POST':
            form = Formulario_profileImage(request.POST, request.FILES)
            if form.is_valid():
                request.user.profile.image = form.cleaned_data['image']
                request.user.profile.save()
                return redirect(Perfil)
        elif request.method == 'GET':
            if request.user.profile.image:
                image = request.user.profile.image
            else:
                image = ''
            form = Formulario_profileImage()     
            context = {
                'form': form,
            'user': request.user.profile.user,
            'phone': request.user.profile.phone,
            'address': request.user.profile.address,
            'image': request.user.profile.image
        }
            return render(request, 'users/profileEditarimage.html', context=context)




@login_required
def Perfil(request):
    try:
        context = {
            'user': request.user.profile.user,
            'phone': request.user.profile.phone,
            'address': request.user.profile.address,
            'image': request.user.profile.image
        }
        return render(request, 'users/profile.html', context=context);
    except:
        User_profile.objects.create(
            user_id = request.user.id
        )
        return render(request, 'inicio.html');
