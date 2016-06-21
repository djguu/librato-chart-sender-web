from django.shortcuts import render, get_object_or_404
from .forms import NewConfigForm
from django.shortcuts import redirect
from .models import Configuration
from db.config_db import ConfigDB


def index(request):
    configurations = Configuration.objects.all()
    return render(request, 'index.html', {'configurations': configurations})


def config_new(request):
    if request.method == "POST":
        form = NewConfigForm(request.POST)
        if form.is_valid():
            ConfigDB.create_configuration(form.get_form_values())
            return redirect('index')
        else:
            error_list = {'error_list': form.get_errors()}
            error_list.update(form.get_form_values())
            return render(request, 'config/new.html', error_list)
    else:
        return render(request, 'config/new.html', {'title': 'New Config',
                                                   'page': 'new'})


def config_edit(request, config_id):
    config = Configuration.objects.get(id=config_id)
    if request.method == "POST":
        form = NewConfigForm(request.POST)
        if form.is_valid():
            ConfigDB.update_configuration(config_id, form.get_form_values())
            return redirect('index')
        else:
            error_list = {'error_list': form.get_errors()}
            error_list.update(form.get_form_values())
            return render(request, 'config/new.html', error_list)
    else:
        return render(request, 'config/new.html', {'title': 'Edit Config',
                                                   'page': 'edit/'+config_id,
                                                   'email_username': config.librato_user,
                                                   'api_key': config.librato_api_key,
                                                   'recipients': config.recipients_emails.split(','),
                                                   'chart_ids': config.chart_ids.split(',')})


def config_delete(request, config_id):
    ConfigDB.delete_configuration(config_id)
    return redirect('index')
