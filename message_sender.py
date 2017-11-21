import pymysql
import datetime
from dateutil.relativedelta import relativedelta
from twilio.rest import Client


def get_messages():

    conn = pymysql.connect(
        host='45.55.47.192',
        user='david',
        password='41willow',
        database='kronos'
    )

    cursor = conn.cursor()
    cursor.execute("CALL todays_messages()")
    data = cursor.fetchall()
    conn.close()

    return data


def update_send_dates(event_id,
                      recurring,
                      warning,
                      interval,
                      interval_delta,
                      warning_interval,
                      warning_interval_delta,
                      is_warning):

    now = datetime.datetime.now()
    if recurring == 0:
        next_send_updated = '9999-12-31'
    else:
        if interval_delta == 'day':
            next_send_updated = now + relativedelta(days=interval)
      #      next_send_updated = datetime.datetime.strftime(next_send_updated, '%Y-%m-%d')
        elif interval_delta == 'week':
            next_send_updated = now + relativedelta(weeks=interval)
       #     next_send_updated = datetime.datetime.strftime(next_send_updated, '%Y-%m-%d')
        elif interval_delta == 'month':
            next_send_updated = now + relativedelta(months=interval)
        #    next_send_updated = datetime.datetime.strftime(next_send_updated, '%Y-%m-%d')
        elif interval_delta == 'year':
            next_send_updated = now + relativedelta(years=interval)
        #    next_send_updated = datetime.datetime.strftime(next_send_updated, '%Y-%m-%d')
        else:
            next_send_updated = '9999-12-31'
    if warning == 1:
        if warning_interval_delta == 'day':
            warning_next_send_updated = next_send_updated - relativedelta(days=warning_interval)
        #    warning_next_send_updated = datetime.datetime.strftime(warning_next_send_updated, '%Y-%m-%d')
        elif warning_interval_delta == 'week':
            warning_next_send_updated = next_send_updated - relativedelta(weeks=warning_interval)
         #   warning_next_send_updated = datetime.datetime.strftime(warning_next_send_updated, '%Y-%m-%d')
        elif warning_interval_delta == 'month':
            warning_next_send_updated = next_send_updated - relativedelta(months=warning_interval)
        #    warning_next_send_updated = datetime.datetime.strftime(warning_next_send_updated, '%Y-%m-%d')
        elif warning_interval_delta == 'year':
            warning_next_send_updated = next_send_updated - relativedelta(years=warning_interval)
         #   warning_next_send_updated = datetime.datetime.strftime(warning_next_send_updated, '%Y-%m-%d')
        else:
            warning_next_send_updated = '9999-12-31'

    else:
        warning_next_send_updated = None

    if is_warning == 0:

        conn = pymysql.connect(
            host='45.55.47.192',
            user='david',
            password='41willow',
            database='kronos'
        )

        cursor = conn.cursor()

        query = "CALL update_next_send('{next_send}', '{warning_next_send}', '{event_id}');".format(
            event_id=event_id,
            next_send=next_send_updated,
            warning_next_send=warning_next_send_updated
        )

        cursor.execute(query)
        conn.commit()
        conn.close()


def update_message_log(messages):
    pass
    #need to figure out django inside of this script...


def send_messages(messages, client):

    for message in messages:
        event_id = message[2]
        phone_number = message[1]
        recurring = message[3]
        message_text = message[0]
        interval = message[4]
        interval_delta = message[5]
        warning_interval = message[6]
        warning_interval_delta = message[7]
        warning = message[8]
        is_warning = message[9]

        phone_number = phone_number.replace(' ', '')
        phone_number = phone_number.replace('-', '')
        phone_number = phone_number.replace(')', '')
        phone_number = phone_number.replace('(', '')

        client.messages.create(
            "{}".format(phone_number),
            body="{}".format(message_text),
            from_="6176124349"
        )

        update_send_dates(event_id,
                      recurring,
                      warning,
                      interval,
                      interval_delta,
                      warning_interval,
                      warning_interval_delta,
                      is_warning)


def main():

    account_sid = "AC2bbc9daa745a839d8014249fc61f45ea"
    auth_token = "adf1c0fc175a946a58d257c0ffaec729"
    twilio_client = Client(account_sid, auth_token)

    todays_messages = get_messages()
    print(todays_messages)

    if len(todays_messages) > 0:
       send_messages(todays_messages, twilio_client)


if __name__ == '__main__':
    main()