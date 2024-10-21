from django.shortcuts import render
from persons.models import Person


def admin_index(request):
    person_list = Person.objects.all()
    context = {
        'person_list': person_list,
    }
    return render(request, 'admin_panel/admin_index.html', context)
