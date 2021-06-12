import requests
import json
import sys

import kakao_api
import log


def get_stock_data(name, itemcode):
    host = "https://api.finance.naver.com"
    path = "/service/itemSummary.nhn"
    url = host + path
    parameter = {'itemcode': itemcode}

    res = requests.get(url, params=parameter)
    if res.status_code != 200:
        log.record_error(4, res.status_code, sys._getframe().f_code.co_name)
        return -1

    data = res.json()

    # revise condition for alarm after
    if data["risefall"] > 3:
        kakao_api.send_to_me(name)

    return data
