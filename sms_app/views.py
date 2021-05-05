from django.http import HttpResponse
from django.shortcuts import render

from sms_app.forms.create_forms import *
from sms_app.models import *


def index(request):
    return HttpResponse('Welcome to SMS')

def retrieve_entry_set(request, entry_name):
    try:
        entries = get_entries()
        entry_set = entries[entry_name]
        context = {
            'entry_name':entry_name.capitalize(),
            'customer_field_names':entry_set.retrieve_customer_field_names(),
            'entry_set':entry_set.objects.all(),
        }
        return render(request, 'sms_app/retrieve_entry_set_view.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist'.format(entry_name))

def retrieve_entry(request, entry_name, id):
    try:
        entries = get_entries()
        entry_set = entries[entry_name]
        entry = entry_set.objects.get(pk=id)
        context = {
            'entry_name':entry_name.capitalize(),

            # 'entry': {
            #     customer_field_name: entry.__dict__[field] for customer_field_name, field in
            #     zip(entry.retrieve_customer_field_names(), entry.retrieve_field_names())
            # }
        }
        return render(request, 'sms_app/retrieve_entry_view.html', context=context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist.'.format(entry_name))
    except ObjectDoesNotExist:
        return HttpResponse('Entry "{}" with ID "{} does not exist"'.format(entry_name, id))


def create_entry(request, entry_name):
    try:
        create_forms = get_create_forms()
        _form = create_forms[entry_name]
        form = _form(request.POST or None)
        if form.is_valid():
            form.save()
        context = {
            'entry_name': entry_name.capitalize(),
            'form':form,
        }
        return render(request, "sms_app/create_view.html", context)
    except KeyError:
        return HttpResponse('Entry "{}" does not exist'.format(entry_name))
