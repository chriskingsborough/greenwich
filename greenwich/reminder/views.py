from django.shortcuts import render, redirect
from reminder.forms import EventForm
from reminder.models import Event
from index.models import User
from reminder import models
import datetime

def add_event(request):

    # redirect to sign in not logged in
    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    # if this is a POST request we need to process the form dat
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        # import pdb; pdb.set_trace()
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_data = form.cleaned_data
            if form_data['warning'] == 1:
                warning_next_send = form_data['start_date'] #plus time delta...
            else:
                warning_next_send = None
            
            current_user = User.objects.get(pk=request.user.id)
            new_row = Event(
                user_id = current_user,
                event_name = form_data['event_name'],
                recurring = form_data['recurring'],
                date_type = form_data['date_type'],
                message = form_data['message'],
                created = datetime.datetime.now(),
                start_date = form_data['start_date'],
                end_date = form_data['end_date'],
                last_send = None,
                next_send = form_data['start_date'],
                interval = form_data['interval'],
                interval_type = form_data['interval_type'],
                snooze = 0,
                snooze_interval = None,
                snooze_interval_type = None,
                snooze_last_send = None,
                snooze_next_send = None,
                warning = form_data['warning'],
                warning_interval = form_data['warning_interval'],
                warning_interval_type = form_data['warning_interval_type'],
                warning_next_send = warning_next_send,
                in_deleted = 0,
            )
            new_row.save()
            return redirect('/')
    else:
        form = EventForm()
    
    #this doesnt really work idk what it is
    #also the next send warning needs to be updated to add the warning time delta
    return render(request, 'reminder/new_event.html', {'form': form})
