import hashlib

headers = {'User-Agent': 'Mozilla/5.0'}


def send_request(pg_id, amount, title):
    payload = {'pg_order_id': str(pg_id),
               'pg_amount': str(amount),
               'pg_description': str(title),
               'pg_merchant_id': '542600',
               'pg_salt': 'goldentravel.uz',
               }

    test_sig = "init_payment.php;"

    secret_key = "Eyq0azWnF7ycyEUE"

    for i in sorted(payload):
        print(i, payload[i], end=' \n')
        test_sig += payload[i] + ';'

    test_sig += secret_key

    pg_sig = hashlib.md5(test_sig.encode('utf-8')).hexdigest()

    payload.update({"pg_sig": pg_sig})
    return payload['pg_sig']
