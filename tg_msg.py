import requests
telegram_creds = ['1495094284:AAFbtoNi-ixIQgyLE0HkXtNqf7fxQy68Xjw__-1001530082955']


def send_mess(text):
    for i in telegram_creds:
        ids = i.split('__')
        token = ids[0]
        id = ids[1]
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={text}&parse_mode=HTML'
        # print(text)
        # logging.info(url)
        requests.get(url)
