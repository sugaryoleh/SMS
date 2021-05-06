from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from sms_app.forms.create_forms import *
from sms_app.models.models import *
from sms_app.validators import access_validator, define_content_by_permission


def index(request):
    content = define_content_by_permission(request)
    context = {
        'content':content,
    }
    return render(request, 'sms_app/main.html', context=context)


def sanatorium_dependent(entry):
    if 'sanatorium' in entry.retrieve_field_names():
        return True
    return False

def get_objects(request, entry):
    if sanatorium_dependent(entry):
        s = Employee.objects.filter(user=request.user)[0].sanatorium
        return entry.objects.filter(sanatorium=s)
    else:
        return entry.objects.all()

@login_required
@access_validator
def retrieve_set(request, entry_name):
    try:
        content = define_content_by_permission(request)
        entries = get_entries()
        entry_set = entries[entry_name]
        context = {
            'entry_name':entry_name,
            'customer_field_names':entry_set.retrieve_customer_field_names(),
            'entry_set':get_objects(request, entry_set),
            'content':content,
        }
        return render(request, 'sms_app/view_set.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist'.format(entry_name))


@login_required
@access_validator
def retrieve(request, entry_name, entry_id):
    try:
        content = define_content_by_permission(request)
        entries = get_entries()
        entry_set = entries[entry_name]
        entry = entry_set.objects.get(pk=entry_id)
        context = {
            'entry_name':entry_name,
            'entry_id':entry_id,
            'entry': entry.customer_dict(),
            'content':content
        }
        return render(request, 'sms_app/view.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist.'.format(entry_name))
    except ObjectDoesNotExist:
        return HttpResponse('Entry "{}" with ID "{}" does not exist'.format(entry_name, entry_id))


@login_required
@access_validator
def create(request, entry_name):
    try:
        content = define_content_by_permission(request)
        create_forms = get_create_forms()
        _form = create_forms[entry_name]
        form = _form(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/sms/view/{}/{}'.format(entry_name, id))
        context = {
            'entry_name': entry_name,
            'form':form,
            'content': content
        }
        return render(request, 'sms_app/create.html', context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist'.format(entry_name))


@login_required
@access_validator
def update(request, entry_name, entry_id):
    try:
        content = define_content_by_permission(request)
        entries = get_entries()
        entry_set = entries[entry_name]
        entry = entry_set.objects.get(pk=entry_id)
        create_forms = get_create_forms()
        _form = create_forms[entry_name]
        form = _form(request.POST or None, instance=entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/sms/view/{}/{}'.format(entry_name, entry_id))
        context = {
            'entry_name':entry_name,
            'form':form,
            'content': content
        }
        return render(request, 'sms_app/change.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist.'.format(entry_name))
    except ObjectDoesNotExist:
        return HttpResponse('Entry "{}" with ID "{}" does not exist'.format(entry_name, entry_id))


@login_required
@access_validator
def delete(request, entry_name, entry_id):
    try:
        content = define_content_by_permission(request)
        entries = get_entries()
        entry_set = entries[entry_name]
        entry = entry_set.objects.get(pk=entry_id)
        context = {
            'entry_name':entry_name,
            'entry_id': entry_id,
            'content': content
        }
        if request.method == 'POST':
            entry.delete()
            return HttpResponseRedirect('http://127.0.0.1:8000/sms/view/{}/'.format(entry_name))
        return render(request, 'sms_app/delete.html', context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist.'.format(entry_name))
    except ObjectDoesNotExist:
        return HttpResponse('Entry "{}" with ID "{}" does not exist'.format(entry_name, entry_id))




