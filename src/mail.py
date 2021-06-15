import json
import smtplib
from email.mime.text import MIMEText

import log


security_FILE_PATH = '/home/kmkim/Projects/security.json'


def send_mail(ent_name):
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

    smtpName = "smtp.naver.com"
    smtpPort = 587

    text = ent_name + " 돔황챠~~"
    msg = MIMEText(text)

    msg['Subject'] = "[주식 알림]"
    msg['From'] = sendEmail
    msg['To'] = recvEmail

    s = smtplib.SMTP(smtpName, smtpPort)  # 메일 서버 연결
    s.starttls()  # TLS 보안 처리
    s.login(sendEmail, password)  # 로그인
    s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환하여 보냅니다.
    s.close()  # smtp 서버 연결을 종료합니다.
