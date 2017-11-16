import pymysql
import datetime
from dateutil.relativedelta import relativedelta
from twilio.rest import Client

account_sid = "AC2bbc9daa745a839d8014249fc61f45ea"

auth_token = "adf1c0fc175a946a58d257c0ffaec729"

client = Client(account_sid, auth_token)


def get_messages():

    conn = pymysql.connect(
        host='192.168.1.18',
        user='Chris',
        password='halo',
        database='kronos'
    )

    cursor = conn.cursor()

    cursor.execute("CALL todays_messages()")

    data = cursor.fetchall()

    conn.close()

    return data

def send_messages(messages):

    for message in messages:
        event_id = message[0]
        event_type = message[1]
        message_text = message[2]
        phone_number = message[3]
        frequency = message[4]

        sent_message = client.messages.create(
            "{}".format(phone_number),
            body="{}".format(message_text),
            from_="6176124349"
        )

        update_send_dates(event_id, event_type, frequency)


def update_send_dates(event_id, event_type, frequency):

    now = datetime.datetime.now()

    if event_type == 'non-recurring':
        next_send = '9999-12-31'
    else:
        if frequency == 'day':
            next_send = now + relativedelta(days=1)
            next_send = datetime.datetime.strftime(next_send, '%Y-%m-%d')
        elif frequency == 'week':
            next_send = now + relativedelta(weeks=1)
            next_send = datetime.datetime.strftime(next_send, '%Y-%m-%d')
        elif frequency == 'month':
            next_send = now + relativedelta(months=1)
            next_send = datetime.datetime.strftime(next_send, '%Y-%m-%d')
        elif frequency == 'year':
            next_send = now + relativedelta(years=1)
            next_send = datetime.datetime.strftime(next_send, '%Y-%m-%d')

    conn = pymysql.connect(
        host='192.168.1.18',
        user='Chris',
        password='halo',
        database='kronos'
    )

    cursor = conn.cursor()

    query = "CALL update_next_send({event_id}, '{next_send}');".format(
        event_id=event_id,
        next_send=next_send
    )

    cursor.execute(query)

    conn.commit()
    conn.close()

def main():

    messages = get_messages()
    if len(messages) > 0:
        send_messages(messages)

if __name__ == '__main__':
    main()
