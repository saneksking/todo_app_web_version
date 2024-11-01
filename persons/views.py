from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from persons.forms import SignUpForm, CreateToDoForm, SettingsForm
from persons.models import Person, ToDo


def login_view(request):
    message = request.session.pop('message', None)
    if request.user.is_authenticated:
        return redirect(reverse('persons:profile', args=(request.user.id, )))
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        temp_user = Person.objects.filter(email=email).first()
        if temp_user:
            if not temp_user.is_active:
                super_user = Person.objects.filter(is_staff=True).first()
                msg = f'Ваш аккаунт заблокирован! Для разблокировки пишите на {super_user.email}.'
                message = {
                    'type': 'danger',
                    'text': msg
                }
                request.session['message'] = message
                return redirect('persons:login')
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
                'text': 'Неверныё e-mail или пароль.',
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
                'text': f'Вы успешно зарегестрировались в системе!'
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
        form = SignUpForm()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'persons/register.html', context)


@login_required
def profile(request, person_id):
    message = request.session.pop('message', None)
    person = Person.objects.get(pk=person_id)
    context = {
        'message': message,
        'person': person
    }
    return render(request, 'persons/profile.html', context)


@login_required
def person_todo_list(request):
    message = request.session.pop('message', None)
    person = Person.objects.get(pk=request.user.id)
    todo_list = ToDo.objects.filter(person=person.id)
    context = {
        'todo_list': todo_list,
        'message': message,
        'person': person
    }
    return render(request, 'persons/todo_list.html', context)


@login_required
def create_todo(request):
    form = CreateToDoForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.person_id = request.user.id
            new_task.save()
            message = {
                'type': 'success',
                'text': f'Задача была успешно создана!'
            }
            request.session['message'] = message
            return redirect('persons:todo_list')
    context = {
        'form': form
    }
    return render(request, 'persons/create_todo.html', context)


@login_required
def delete_todo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.delete()
    message = {
        'type': 'success',
        'text': f'Задача была успешно удалена!'
    }
    request.session['message'] = message
    return redirect('persons:todo_list')


@login_required
def update_todo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    form = CreateToDoForm(request.POST or None, instance=todo)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            message = {
                'type': 'success',
                'text': f'Задача была успешно изменена!'
            }
            request.session['message'] = message
            return redirect('persons:todo_list')
        else:
            form = CreateToDoForm(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'persons/update_todo.html', context)


@login_required
def change_todo_status(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    todo.status = not todo.status
    todo.save()
    if todo.status:
        message = {
            'type': 'success',
            'text': f'Задача была успешно выполнена!'
        }
    else:
        message = {
            'type': 'success',
            'text': f'Задача была успешно помечена невыполненной!'
        }
    request.session['message'] = message
    return redirect('persons:todo_list')


@login_required
def profile_settings(request):
    person = Person.objects.get(pk=request.user.id)
    form = SettingsForm(request.POST or None, instance=person)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            message = {
                'type': 'success',
                'text': f'Настройки были успешно применены!'
            }
            request.session['message'] = message
            return redirect(reverse('persons:profile', args=(person.id, )))
        else:
            form = SettingsForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'persons/profile_settings.html', context)
