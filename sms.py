from pprint import pprint
from smsaero import SmsAero, SmsAeroException


SMSAERO_EMAIL = 'evgenc1980@mail.ru'
SMSAERO_API_KEY = 'tJuLoVucxZaSxxO8xKmAfoilFD6'

def send_sms(phone: int, message: str) -> dict:
    api = SmsAero(SMSAERO_EMAIL, SMSAERO_API_KEY)
    return api.send_sms(phone, message)


if __name__ == '__main__':
 try:
    result = send_sms(79231917044, 'Hello, World!')
    pprint(result)
 except SmsAeroException as e:
    print(f"An error occurred:  {e}")