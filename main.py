import requests
import json
import openpyxl
import datetime


def search(num):
    if num == 1:
        itemcode = "005930"
    elif num == 2:
        itemcode = "035720"
    elif num == 3:
        itemcode = "000660"
    elif num == 4:
        itemcode = "035420"

    host = 'http://api.finance.naver.com'
    path = '/service/itemSummary.nhn'
    param = {'itemcode': itemcode}
    url = host + path

    res = requests.get(url, params=param)
    if res.status_code != 200:
        print("API Get Failed")
        quit()

    data = res.json()
    save(data, num)


def save(data, itemcode):
    dt_now = datetime.datetime.now()

    risefall = data["risefall"]
    if risefall == 1:
        rf = "상한"
    elif risefall == 2:
        rf = "상승"
    elif risefall == 3:
        rf = "보합"
    elif risefall == 4:
        rf = "하한"
    else:
        rf = "하락"

    wb = openpyxl.load_workbook(
        '/home/kmkim/Projects/git/kmkim036/Stock-Manage/data.xlsx')

    if itemcode == 1:
        ws = wb['samsung']
    elif itemcode == 2:
        ws = wb['kakao']
    elif itemcode == 3:
        ws = wb['SKhynix']
    else:
        ws = wb['naver']

    ws.append([dt_now.date(), data["marketSum"], data["per"], data["eps"], data["pbr"], data["now"],
              data["diff"], data["rate"], data["quant"], data["amount"], data["high"], data["low"], rf])
    wb.save('/home/kmkim/Projects/git/kmkim036/Stock-Manage/data.xlsx')
    wb.close()


for i in range(1, 5):
    search(i)
