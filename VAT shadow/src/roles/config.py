from .models import PrivilageMaster


def add_privilage():
    permissions = [
        'Manage Roles & Permissions', 'User Management',
        'Audit Task Management', 'Verify Asset Task',
        'Initial Data Upload Access', 'Report Access'
    ]

    for i in permissions:
        if not PrivilageMaster.objects.filter(name=i).exists():
            privilage = PrivilageMaster.objects.create(name=i)
