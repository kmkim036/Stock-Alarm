import sys
import requests
import json

import log


security_FILE_PATH = '/home/kmkim/Projects/security.json'


def check_refresk_token(json):
    try:
        buf = json['refresh_token']
    except KeyError:
        return False
    return True


def get_token():
    try:
        with open(security_FILE_PATH) as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        log.record_error(2, 0, sys._getframe().f_code.co_name)
        return

    host = "https://kauth.kakao.com"
    path = "/oauth/token"
    url = host + path

    restapi_key = json_data['kakao']['restapi-key']
    redirect_uri = json_data['kakao']['redirect-uri']
    code = json_data['kakao']['code']

    parameter = {
        'grant_type': 'authorization_code',
        'client_id': restapi_key,
        'redirect_uri': redirect_uri,
        'code': code
    }

    res = requests.post(url, params=parameter)
    if res.status_code != 200:
        log.record_error(3, res.status_code, sys._getframe().f_code.co_name)
        return -1

    data = res.json()

    json_data['kakao']['access-token'] = data['access_token']
    json_data['kakao']['refresh-token'] = data['refresh_token']

    try:
        with open(security_FILE_PATH, 'w', encoding='utf-8') as make_file:
            json.dump(json_data, make_file, indent="\t")
    except FileNotFoundError:
        log.record_error(2, 0, sys._getframe().f_code.co_name)
        return


def refresh_token():
    try:
        with open(security_FILE_PATH) as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        log.record_error(2, 0, sys._getframe().f_code.co_name)
        return

    host = "https://kauth.kakao.com"
    path = "/oauth/token"
    url = host + path

    restapi_key = json_data['kakao']['restapi-key']
    refresh_token = json_data['kakao']['refresh-token']

    parameter = {
        'grant_type': 'refresh_token',
        'client_id': restapi_key,
        'refresh_token': refresh_token
    }

    res = requests.post(url, params=parameter)
    if res.status_code != 200:
        log.record_error(3, res.status_code, sys._getframe().f_code.co_name)
        return -1

    data = res.json()

    json_data['kakao']['access-token'] = data['access_token']
    if check_refresk_token == True:
        json_data['kakao']['refresh-token'] = data['refresh_token']

    try:
        with open(security_FILE_PATH, 'w', encoding='utf-8') as make_file:
            json.dump(json_data, make_file, indent="\t")
    except FileNotFoundError:
        log.record_error(2, 0, sys._getframe().f_code.co_name)
        return


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
        with open(security_FILE_PATH) as json_file:
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
