import requests
import json
import sys

import log


def check_access_token(access_token):
    host = "https://kapi.kakao.com"
    path = "/v1/user/access_token_info"
    url = host + path
    header = {"Authorization": 'Bearer ' + access_token}

    res = requests.get(url, headers=header)
    if res.status_code != 200:
        log.record_error(4, res.status_code, sys._getframe().f_code.co_name)
        return -1

    data = res.json()

    if(data["expires_in"] < 1):
        log.record_error(5, 0, sys._getframe().f_code.co_name)
        return -2

    return 0


def send_to_me(ent_name):
    log.record_kakao_send(ent_name)

    try:
        with open('/home/kmkim/Projects/security.json') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        log.record_error(2, 0, sys._getframe().f_code.co_name)
        return

    ACCESS_TOKEN = json_data["kakao"]["access-token"]
    if check_access_token(ACCESS_TOKEN) != 0:
        return

    host = "https://kapi.kakao.com"
    path = "/v2/api/talk/memo/default/send"
    url = host + path
    header = {"Authorization": 'Bearer ' + ACCESS_TOKEN}
    body = {
        "object_type": "text",
        "text": ent_name + " 돔황챠~~",
        "link": {
            "web_url": "https://developers.kakao.com"
        }
    }
    body_json = {"template_object": json.dumps(body)}

    res = requests.post(url, headers=header, data=body_json)
    if res.status_code != 200:
        log.record_error(3, res.status_code, sys._getframe().f_code.co_name)

    return
