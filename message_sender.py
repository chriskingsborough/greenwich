import pymysql
import datetime
from dateutil.relativedelta import relativedelta
from twilio.rest import Client


def get_messages():

    conn = pymysql.connect(
        host='45.55.47.192',
        user='david',
        password='Celtics1!',
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

    if is_warning == 1:
        pass

    else:
        if recurring == 0:
            next_send_updated = '9999-12-31'
            warning_next_send_updated = '9999-12-31'

        else:
            if interval_delta == 'day':
                next_send_updated = now + relativedelta(days=interval)
            elif interval_delta == 'week':
                next_send_updated = now + relativedelta(weeks=interval)
            elif interval_delta == 'month':
                next_send_updated = now + relativedelta(months=interval)
            elif interval_delta == 'year':
                next_send_updated = now + relativedelta(years=interval)
            else:
                next_send_updated = '9999-12-31'

            if warning == 1:
                if warning_interval_delta == 'day':
                    warning_next_send_updated = next_send_updated - relativedelta(days=warning_interval)
                elif warning_interval_delta == 'week':
                    warning_next_send_updated = next_send_updated - relativedelta(weeks=warning_interval)
                elif warning_interval_delta == 'month':
                    warning_next_send_updated = next_send_updated - relativedelta(months=warning_interval)
                elif warning_interval_delta == 'year':
                    warning_next_send_updated = next_send_updated - relativedelta(years=warning_interval)

        conn = pymysql.connect(
            host='45.55.47.192',
            user='david',
            password='Celtics1!',
            database='kronos'
        )

        query = "CALL update_next_send('{next_send}','{warning_next_send}','{event_id}');".format(
            event_id=event_id,
            next_send=next_send_updated,
            warning_next_send=warning_next_send_updated
        )

        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()


def update_message_log(event_id,user_id,phone_number):
    conn = pymysql.connect(
        host='45.55.47.192',
        user='david',
        password='Celtics1!',
        database='kronos'
    )

    sql = "insert into reminder_messagelog (user_id, event_id , sent, phone_number)\
    values('{}','{}','{}','{}')".format(
        user_id, event_id,  datetime.datetime.now(), phone_number)

    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


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
        user_id = message[10]

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

        update_message_log(event_id,
                           user_id,
                           phone_number)


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
