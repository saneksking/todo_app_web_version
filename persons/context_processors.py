from persons.models import ToDo


def todo_count(request):
    return {'todo_count': ToDo.objects.filter(person_id=request.user.id).count()}
