from django.shortcuts import render
from reminder.forms import EventForm

def add_event(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_data = form.cleaned_data()
            new_event = Event
            if form_data['warning'] == 1:
                warning_next_send = form_data['event_date'] #plus time delta...
            else:
                warning_next_send = None
            new_row = Event.objects.create(
                user_id = models.ForeignKey(auth_user, on_delete=models.CASCADE),
                event_name = form_data['event_name'],
                recurring = form_data['recurring'],
                date_type = form_data['date_type'],
                message = form_data['message'],
                created = datetime.datetime.now(),
                start_date = form_data['event_date'],
                end_date = form_data['end_date'],
                last_send = None,
                next_send = form_data['event_date'],
                interval = form_data['interval'],
                interval_type = form_data['interval_type'],
                snooze = 0,
                snooze_interval = None,
                snooze_interval_type = None,
                snooze_last_send = None,
                snooze_next_send = None,
                warning = form_data['warning'],
                warning_interval = form_data['warning_interval'],
                warning_interval_type = form_data['warning_interval'],
                warning_next_send = warning_next_send,
                in_deleted = 0,
            )
    else:
        form = EventForm()
    

    return render(request, 'reminder/new_event.html', {'form': form})