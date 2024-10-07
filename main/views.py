from django.shortcuts import render

from persons.models import Person


def home(request):
    message = request.session.pop('message', None)
    context = {
        'message': message,
    }
    return render(request, 'main/home.html', context)
