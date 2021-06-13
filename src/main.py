import sys
import datetime
import json
import openpyxl

import log
import naver_api


data_FILE_PATH = '/home/kmkim/Projects/git/kmkim036/Stock-Manage/data/data.xlsx'


class Enterprise:
    def __init__(self, name, itemcode):
        self.name = name
        self.itemcode = itemcode

    def get_data(self):
        ret = naver_api.get_stock_data(self.name, self.itemcode)
        if ret == -1:
            return
        else:
            self.save(ret)

    def save(self, data):
        try:
            wb = openpyxl.load_workbook(data_FILE_PATH)
            ws = wb[self.name]
        except FileNotFoundError:
            log.record_error(2, 0, sys._getframe().f_code.co_name)
            return

        A_lastrow = 'A' + str(ws.max_row)
        dt_now = datetime.datetime.now()
        if dt_now.date() < ws[A_lastrow].value.date():
            log.record_error(1, 0, sys._getframe().f_code.co_name)
            wb.close()
            return

        if dt_now.date() == ws[A_lastrow].value.date():
            ws.delete_rows(ws.max_row)

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

        ws.append([dt_now.date(), data["marketSum"], data["per"], data["eps"], data["pbr"], data["now"],
                   data["diff"], data["rate"], data["quant"], data["amount"], data["high"], data["low"], rf])
        wb.save(data_FILE_PATH)
        wb.close()


e1 = Enterprise("samsung", "005930")
e1.get_data()

e2 = Enterprise("kakao", "035720")
e2.get_data()

e3 = Enterprise("SKhynix", "000660")
e3.get_data()

e4 = Enterprise("naver", "035420")
e4.get_data()
