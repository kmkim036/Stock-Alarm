import requests
import json
import openpyxl
import datetime


class enterprise:
    def __init__(self, name, itemcode):
        self.name = name
        self.itemcode = itemcode

    def search(self):
        host = 'http://api.finance.naver.com'
        path = '/service/itemSummary.nhn'
        param = {'itemcode': self.itemcode}
        url = host + path
        res = requests.get(url, params=param)
        if res.status_code != 200:
            print("ERROR:" + "API Get Failed in " + self.name)
            return
        data = res.json()
        self.save(data)

    def save(self, data):
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

        ws = wb[self.name]

        A_lastrow = 'A' + str(ws.max_row)

        if dt_now.date() < ws[A_lastrow].value.date():
            print("ERROR: "+ "Date overflow in " + self.name)
            return

        if dt_now.date() == ws[A_lastrow].value.date():
            ws.delete_rows(ws.max_row)

        ws.append([dt_now.date(), data["marketSum"], data["per"], data["eps"], data["pbr"], data["now"],
                   data["diff"], data["rate"], data["quant"], data["amount"], data["high"], data["low"], rf])
        wb.save('/home/kmkim/Projects/git/kmkim036/Stock-Manage/data.xlsx')
        wb.close()


e1 = enterprise("samsung", "005930")
e1.search()

e2 = enterprise("kakao", "035720")
e2.search()

e3 = enterprise("SKhynix", "000660")
e3.search()

e4 = enterprise("naver", "035420")
e4.search()
