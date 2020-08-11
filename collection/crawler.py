import sys
from datetime import datetime
from urllib.request import Request, urlopen


def error_defalut(e):
    print(f'{e} : {datetime.now}', file=sys.stderr)


def crawling(
        url='',
        encoding='utf-8',
        error=lambda e: print(f'{e} : {datetime.now}', file=sys.stderr),
        # proc1=lambda d: d
        ):
    try:
        request = Request(url)
        response = urlopen(request)
        print(f'{datetime.now}: sucess for request[{url}]')

        receive = response.read().decode(encoding, errors='replace')
        # return proc1(receive)
        return receive

    except Exception as e:
        if error is not None:
            error(e)
