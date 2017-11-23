from django.shortcuts import render, redirect
from reminder.forms import EventForm
from reminder.models import Event
from index.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView


import datetime
from dateutil.relativedelta import relativedelta

def add_event(request):

    # redirect to sign in not logged in
    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    # if this is a POST request we need to process the form dat
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_data = form.cleaned_data

            if form_data['warning'] == 1:
                if form_data['warning_interval_type'] == 'day':
                    warning_next_send = form_data['start_date'] \
                                        - relativedelta(days=form_data['warning_interval'])
                elif form_data['warning_interval_type'] == 'week':
                    warning_next_send = form_data['start_date'] \
                                        - relativedelta(weeks=form_data['warning_interval'])
                elif form_data['warning_interval_type'] == 'month':
                    warning_next_send = form_data['start_date'] \
                                        - relativedelta(months=form_data['warning_interval'])
                elif form_data['warning_interval_type'] == 'year':
                    warning_next_send = form_data['start_date'] \
                                        - relativedelta(years=form_data['warning_interval'])
                else:
                    warning_next_send = None
            else:
                warning_next_send = None
            
            current_user = User.objects.get(pk=request.user.id)
            new_row = Event(
                user=current_user,
                event_name=form_data['event_name'],
                recurring=form_data['recurring'],
                message=form_data['message'],
                created=datetime.datetime.now(),
                start_date=form_data['start_date'],
                end_date=form_data['end_date'],
                last_send=None,
                next_send=form_data['start_date'],
                interval=form_data['interval'],
                interval_type=form_data['interval_type'],
                snooze=0,
                snooze_interval=None,
                snooze_interval_type=None,
                snooze_last_send=None,
                snooze_next_send=None,
                warning=form_data['warning'],
                warning_interval=form_data['warning_interval'],
                warning_interval_type=form_data['warning_interval_type'],
                warning_next_send=warning_next_send,
                in_deleted=0,
            )
            new_row.save()
            return redirect('/view_reminders/')
    else:
        form = EventForm()

    return render(request, 'reminder/new_event.html', {'form': form})


def view_events(request):

    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    events = Event.objects.filter(user_id=request.user.id).reverse()

    context = {'events': events}

    return render(request, 'reminder/view_reminders.html', context)

def edit_event(request):

    if 'id' not in request.session.keys():
        return redirect('/sign_in/')
    #TODO: check to make sure user logged in is associated with event - event ID may be public in the URL

    # get event ID from querystring
    event_id = request.GET['id']
    # pass event ID to Event model to pull current event
    current_event = Event.objects.get(pk=event_id)

    form = EventForm(request.POST or None, instance=current_event)
    if request.POST and form.is_valid():
        form.save()

        # Save was successful
        redirect_url = '/view_reminders/'
        return redirect(redirect_url)

    context = {'form': form}

    return render(request, 'reminder/edit_reminder.html', context=context)

def view_reminder(request):
    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    event_id = request.GET['id']

    current_event = Event.objects.get(pk=event_id)

    context = {'event': current_event}

    return render(request, 'reminder/view_reminder.html', context=context)

def delete_reminder(request):
    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    event_id = request.GET['id']

    current_event = Event.objects.get(pk=event_id)

    current_event.delete()

    return redirect('/view_reminders/')
