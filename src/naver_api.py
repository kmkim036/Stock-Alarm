import sys
import requests
import json

import log


def get_stock_data(name, itemcode):
    host = "https://api.finance.naver.com"
    path = "/service/itemSummary.nhn"
    url = host + path
    parameter = {'itemcode': itemcode}

    res = requests.get(url, params=parameter)

    if res.status_code != 200:
        msg = "API GET failed, status code: " + \
            str(res.status_code) + ", error desc: wrong url"
        log.record_error(msg, sys._getframe().f_code.co_name)
        return -1

    if res.text == '':
        msg = "API GET failed, error desc: wrong itemcode"
        log.record_error(msg, sys._getframe().f_code.co_name)
        return -2

    return res.json()
