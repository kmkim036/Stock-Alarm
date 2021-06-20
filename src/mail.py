import sys
import datetime
import json
import smtplib
from email.mime.text import MIMEText

import log


security_FILE_PATH = '/home/kmkim/Projects/security.json'


def send_mail(ent_name, state):
    log.record_mail_send(ent_name)
    try:
        with open(security_FILE_PATH) as json_file:
            json_data = json.load(json_file)
    except FileNotFoundError:
        log.record_error(2, 0, sys._getframe().f_code.co_name)
        return

    sendEmail = json_data["naver"]["id"]
    password = json_data["naver"]["pw"]
    recvEmail = json_data["google"]["id"]

    dt_now = datetime.datetime.now()

    smtpName = "smtp.naver.com"
    smtpPort = 587

    if state == 1:
        text = "lower than threshold in " + ent_name
    elif state == 2:
        text = "upper than threshold in " + ent_name
    msg = MIMEText(text)

    msg['Subject'] = "[주식 알림] at " + str(dt_now.date())
    msg['From'] = sendEmail
    msg['To'] = recvEmail

    s = smtplib.SMTP(smtpName, smtpPort)
    s.starttls()
    s.login(sendEmail, password)
    s.sendmail(sendEmail, recvEmail, msg.as_string())
    s.close()
