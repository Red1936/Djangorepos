# C:\Users\Administrador\Documents\APIDjango9ISC22\api\test_forms.py

import pytest
from django.contrib.auth.models import User

from .forms import CustomUserCreationForm


@pytest.mark.django_db
def test_clean_email_unique():
    # Crea un usuario de prueba con el mismo correo electrónico
    User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    # Intenta crear un formulario con el mismo correo electrónico
    form_data = {
        'username': 'newuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'test@example.com',
        'password1': 'newpassword',
        'password2': 'newpassword',
    }
    form = CustomUserCreationForm(data=form_data)

    # Asegúrate de que el formulario no sea válido debido al correo electrónico duplicado
    assert not form.is_valid()
    assert 'Este correo electrónico ya está registrado' in form.errors['email']

@pytest.mark.django_db
def test_clean_email_unique_pass():
    # Intenta crear un formulario con un correo electrónico único
    form_data = {
        'username': 'newuser',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'new@example.com',
        'password1': 'newpassword',
        'password2': 'newpassword',
    }
    form = CustomUserCreationForm(data=form_data)

    # Asegúrate de que el formulario sea válido
    assert form.is_valid()
