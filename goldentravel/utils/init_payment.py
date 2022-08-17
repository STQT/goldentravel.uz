import hashlib

import requests
from bs4 import BeautifulSoup
from goldentravel.applications.models import Application
from django.conf import settings

headers = {'User-Agent': 'Mozilla/5.0'}


def send_request(application: Application):
    payload = {'pg_order_id': str(application.id),
               'pg_amount': str(application.tour.amount),
               'pg_description': application.tour.title,
               'pg_merchant_id': '542600',
               'pg_salt': 'goldentravel.uz',
               # 'pg_can_reject': '1',
               'pg_ps_currency': 'UZS',
               'pg_payment_method': 'bankcard',
               'pg_check_url': '{}/check/'.format(settings.SITE_URL),
               'pg_result_url': '{}/result/'.format(settings.SITE_URL),
               'pg_request_method': 'POST',
               'pg_success_url': '{}/success/'.format(settings.SITE_URL),
               'pg_failure_url': '{}/failure/'.format(settings.SITE_URL),
               'pg_user_contact_email':  application.email,
               }
    test_sig = "init_payment.php;"

    secret_key = "Eyq0azWnF7ycyEUE"

    for i in sorted(payload):
        print(i, payload[i], end=' \n')
        test_sig += payload[i] + ';'

    test_sig += secret_key

    pg_sig = hashlib.md5(test_sig.encode('utf-8')).hexdigest()
    print("SIG,", pg_sig)
    payload.update({"pg_sig": pg_sig})
    x = requests.post('https://api.paybox.money/init_payment.php', headers=headers, data=payload)
    soup = BeautifulSoup(x.content, features="xml")
    return soup.find('pg_redirect_url').text
