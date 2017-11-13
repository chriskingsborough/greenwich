from django.shortcuts import render

import pymysql

# Create your views here.
def create_reminder(request):

    return render(request, 'reminder/create_reminder.html')

def add_reminder(request):

    # check method of request is POST
    if request.method == 'POST':

        # extract data from request
        data = request.POST
    
        # insert a user
        insert_event(data)

    return render(request, 'reminder/reminder_created.html')

def insert_event(data):
    """insert an event"""

    conn = pymysql.connect(
        host='192.168.1.18',
        user='Chris',
        password='halo',
        database='kronos'
    )

    cursor = conn.cursor()

    clean_data = {}

    for key, value in data.items():

        clean_data[key] = value 

    if 'event_type' not in clean_data:
        clean_data['event_type'] = 'non-recurring'

    query = """
    CALL insert_event('{event_name}', '{event_type}', '{event_message}', '{recurrance_frequency}', 1, '{start_date}', '{end_date}')
    """.format(
        **clean_data
    )

    cursor.execute(query)

    cursor.close()

    conn.commit()
    conn.close()
