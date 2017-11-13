from django.shortcuts import render
from django.http import HttpResponseRedirect

import pymysql
import random

# Insert a user
def insert_user(data):

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


    query = """
    INSERT INTO account (accountName, firstName, lastName, email, phoneNumber)
    VALUES ('{username}', '{first_name}', '{last_name}', '{email}', '{phone_number}')
    """.format(
        **clean_data
    )

    cursor.execute(query)

    cursor.close()

    conn.commit()
    conn.close()

# Create your views here.
def register(request):

    return render(request, 'register/registration.html')

def create_account(request):

    # check method of request is POST
    if request.method == 'POST':

        # extract data from request
        data = request.POST
    
        # insert a user
        insert_user(data)

    return render(request, 'register/registration_complete.html')