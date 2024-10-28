from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

from admin_panel.decorators import is_superuser
from admin_panel.forms import AdminSettingsForm
from persons.models import Person


@user_passes_test(is_superuser)
def admin_index(request):
    message = request.session.pop('message', None)
    person_list = Person.objects.all()
    context = {
        'person_list': person_list,
        'message': message,
    }
    return render(request, 'admin_panel/admin_index.html', context)


@user_passes_test(is_superuser)
def person_change_activity(request, person_id):
    person = Person.objects.get(pk=person_id)
    person.switcher_activity()
    person.save()
    message = {
        'type': 'success',
        'text': f'Статус пользователя был успешно изменён!'
    }
    request.session['message'] = message
    return redirect('admin_panel:admin_index')


@user_passes_test(is_superuser)
def person_change_admin_status(request, person_id):
    person = Person.objects.get(pk=person_id)
    person.switcher_administration()
    person.save()
    message = {
        'type': 'success',
        'text': f'Статус пользователя был успешно изменён!'
    }
    request.session['message'] = message
    return redirect('admin_panel:admin_index')


@user_passes_test(is_superuser)
def admin_person_settings(request, person_id):
    person = Person.objects.get(pk=person_id)
    form = AdminSettingsForm(request.POST or None, instance=person)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            message = {
                'type': 'success',
                'text': f'Информация о пользователе была успешно изменена!'
            }
            request.session['message'] = message
            return redirect('admin_panel:admin_index')
        else:
            form = AdminSettingsForm(request.POST)
    context = {
        'form': form,
        'person': person,
    }
    return render(request, 'admin_panel/admin_person_settings.html', context)


@user_passes_test(is_superuser)
def admin_person_delete(request, person_id):
    person = Person.objects.get(pk=person_id)
    person.delete()
    message = {
        'type': 'success',
        'text': f'Пользвоатель был успешно удалён!'
    }
    request.session['message'] = message
    return redirect('admin_panel:admin_index')
