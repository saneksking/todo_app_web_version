from django.shortcuts import render


def admin_index(request):
    context = {

    }
    return render(request, 'admin_panel/admin_index.html', context)
