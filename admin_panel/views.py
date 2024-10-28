from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

from admin_panel.decorators import is_superuser
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
    person.switcher()
    person.save()
    message = {
        'type': 'success',
        'text': f'Статус пользователя был успешно изменён!'
    }
    request.session['message'] = message
    return redirect('admin_panel:admin_index')