

def is_superuser(user):
    return user.is_superuser or user.is_staff
