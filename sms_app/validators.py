from django.http import HttpResponse

from sms_app.apps import SmsAppConfig
from sms_app.models.models import get_entries


def access_validator(function):
    def wrap(request, *args, **kwargs):
        mode = request.get_full_path().split('/')[2]
        entries = get_entries().keys()
        requested_entry = kwargs['entry_name'].replace('_', '')
        for group in request.user.groups.all():
            if '{}_{}'.format(mode, requested_entry) in [perm.codename for perm in group.permissions.all()]:
                return function(request, *args, **kwargs)
        return HttpResponse('perm denied or no such page')

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def can_add(request, entry_name):
    for group in request.user.groups.all():
        if 'add_{}'.format(entry_name.replace('_', '')) in [perm.codename for perm in group.permissions.all()]:
            return True
    return False

def can_change(request, entry_name):
    for group in request.user.groups.all():
        if 'change_{}'.format(entry_name.replace('_', '')) in [perm.codename for perm in group.permissions.all()]:
            return True
    return False

def can_delete(request, entry_name):
    for group in request.user.groups.all():
        if 'delete_{}'.format(entry_name.replace('_', '')) in [perm.codename for perm in group.permissions.all()]:
            return True
    return False

def define_content_by_permission(request):
    app_name = SmsAppConfig.name
    for group in request.user.groups.all():
        l = [str(perm).split('|')[1].rstrip().strip() for perm in group.permissions.all() if
             str(perm).startswith(app_name)]
    l = set(l)
    content = dict(zip([el.capitalize() for el in l], [el.replace(' ', '_') for el in l]))
    return content
