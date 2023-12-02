from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage, send_mail
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from rest_framework.views import APIView

from api.forms import CustomUserCreationForm


class Home(APIView):
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name)
    
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def products(request):
    return render(request, 'core/products.html')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            contact(request)
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)



def contact(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        #subject=request.POST['subject']
        #message=request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': username,
            'email': email,
            #'message': message
        })
        
        email = EmailMessage(
            subject='Confirmacion de registro',
            body=template,
            from_email=settings.EMAIL_HOST_USER,
            to=[email]
         )
        
        email.fail_silenty = False
        email.send()
        messages.success(request, "Registro exitoso se ha enviado un mensaje a tu correo")
        return redirect('home')


def exit(request):
    logout(request)
    return redirect('home')


class carrito():
    def get(self, request):
        # Lógica para mostrar el contenido del carrito
        # Puedes obtener los videojuegos del carrito desde el usuario actual
        # y renderizarlos en un template
        videojuegos_en_carrito = []  # ¡Asegúrate de obtener los videojuegos correctamente!
        total_del_carrito = sum(videojuego.precio for videojuego in videojuegos_en_carrito)
        return render(request, 'carrito.html', {'videojuegos_en_carrito': videojuegos_en_carrito, 'total_del_carrito': total_del_carrito})

class comprar():
    def get(self, request, videojuego_id):
        # Lógica para agregar el videojuego al carrito
        # Puedes obtener el videojuego por su ID y agregarlo al carrito del usuario actual
        # videojuego = Videojuego.objects.get(pk=videojuego_id)
        # Agrega el videojuego al carrito del usuario (debes implementar esta lógica)

        # Después de agregar, redirige a la página del carrito
        return redirect('carrito')





