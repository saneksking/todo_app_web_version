from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from persons.forms import SignUpForm


def login_view(request):
    message = request.session.pop('message', None)
    if request.user.is_authenticated:
        return redirect('persons:profile')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            message = {
                'type': 'success',
                'text': f'{user.full_name}. Добро пожаловать в ToDo App Web'
            }
            request.session['message'] = message
            return redirect('main:home')
        else:
            message = {
                'type': 'danger',
                'text': 'Неверныё e-mail или пароль',
            }
            return render(request, 'persons/login.html', {'message': message})
    context = {
        'message': message
    }
    return render(request, 'persons/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('persons:login')


def register(request):
    if request.user.is_authenticated:
        return redirect('persons:profile')
    message = request.session.pop('message', None)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            message = {
                'type': 'success',
                'text': f'Вы успешно зарегестрировались в системе!!.'
            }
            request.session['message'] = message
            return redirect('persons:login')
        else:
            message = {
                'type': 'danger',
                'text': f'Ошибка! Пользователь с таким e-mail уже зарегистирован!.'
            }
            request.session['message'] = message
    else:
        form = SignUpForm
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'persons/register.html', context)