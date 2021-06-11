import requests
import json
import sys


def check_access_token(access_token):
    header = {"Authorization": 'Bearer ' + access_token}
    url = "https://kapi.kakao.com/v1/user/access_token_info"
    res = requests.get(url, headers=header)

    if res.status_code != 200:
        print(res.status_code)
        print("ERROR: " + "Get API in " + sys._getframe().f_code.co_name)
    data = res.json()

    if(data["expires_in"] < 1):
        print("ERROR: " + "Access token expired in " +
              sys._getframe().f_code.co_name)


def send_to_me(ent_name):
    try:
        with open('/home/kmkim/Projects/security.json') as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        print("ERROR: " + "File 'security.json' open error in " + ent_name)
        return

    ACCESS_TOKEN = json_data["kakao"]["access-token"]
    check_access_token(ACCESS_TOKEN)

    header = {"Authorization": 'Bearer ' + ACCESS_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

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
        print(res.status_code)
        print("ERROR: " + "post kakao-self-send API in " + ent_name)

    return
