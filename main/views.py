from django.shortcuts import render


def home(request):
    message = request.session.pop('message', None)
    context = {
        'message': message,
    }
    return render(request, 'main/home.html', context)
