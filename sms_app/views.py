from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from sms_app.forms.create_forms import *
from sms_app.models.models import *


def index(request):
    return render(request, 'sms_app/main.html')


def retrieve_set(request, entry_name):
    try:
        entries = get_entries()
        entry_set = entries[entry_name]
        context = {
            'entry_name':entry_name,
            'customer_field_names':entry_set.retrieve_customer_field_names(),
            'entry_set':entry_set.objects.all(),
        }
        return render(request, 'sms_app/retrieve_set.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist'.format(entry_name))


def retrieve(request, entry_name, entry_id):
    try:
        entries = get_entries()
        entry_set = entries[entry_name]
        entry = entry_set.objects.get(pk=entry_id)
        context = {
            'entry_name':entry_name,
            'entry_id':entry_id,
            'entry': entry.customer_dict()
        }
        return render(request, 'sms_app/retrieve.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist.'.format(entry_name))
    except ObjectDoesNotExist:
        return HttpResponse('Entry "{}" with ID "{}" does not exist'.format(entry_name, entry_id))


def create(request, entry_name):
    try:
        create_forms = get_create_forms()
        _form = create_forms[entry_name]
        form = _form(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/sms/retrieve/{}/{}'.format(entry_name, id))
        context = {
            'entry_name': entry_name,
            'form':form,
        }
        return render(request, 'sms_app/create.html', context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist'.format(entry_name))


def update(request, entry_name, entry_id):
    try:
        entries = get_entries()
        entry_set = entries[entry_name]
        entry = entry_set.objects.get(pk=entry_id)
        create_forms = get_create_forms()
        _form = create_forms[entry_name]
        form = _form(request.POST or None, instance=entry)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/sms/retrieve/{}/{}'.format(entry_name, entry_id))
        context = {
            'entry_name':entry_name,
            'form':form,
        }
        return render(request, 'sms_app/update.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist.'.format(entry_name))
    except ObjectDoesNotExist:
        return HttpResponse('Entry "{}" with ID "{}" does not exist'.format(entry_name, entry_id))


def delete(request, entry_name, entry_id):
    try:
        entries = get_entries()
        entry_set = entries[entry_name]
        entry = entry_set.objects.get(pk=entry_id)
        context = {
            'entry_name':entry_name,
            'entry_id': entry_id,
        }
        if request.method == 'POST':
            entry.delete()
            return HttpResponseRedirect('http://127.0.0.1:8000/sms/retrieve/{}/'.format(entry_name))
        return render(request, 'sms_app/delete.html', context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist.'.format(entry_name))
    except ObjectDoesNotExist:
        return HttpResponse('Entry "{}" with ID "{}" does not exist'.format(entry_name, entry_id))


