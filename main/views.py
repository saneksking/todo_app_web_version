from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from persons.models import Person


@login_required
def home(request):
    message = request.session.pop('message', None)
    context = {
        'message': message,
    }
    return render(request, 'main/home.html', context)
