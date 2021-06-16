import datetime


kakao_send_log_FILE_PATH = '/home/kmkim/Projects/git/kmkim036/Stock-Alarm/log/kakao_send.log'
error_log_FILE_PATH = '/home/kmkim/Projects/git/kmkim036/Stock-Alarm/log/error.log'
mail_send_log_FILE_PATH = '/home/kmkim/Projects/git/kmkim036/Stock-Alarm/log/mail_send.log'


def record_mail_send(ent_name):
    try:
        f = open(mail_send_log_FILE_PATH, 'a')
    except FileNotFoundError:
        return

    f.write(str(datetime.datetime.now()) + ": " + ent_name + "\n")
    f.close()


def record_kakao_send(ent_name):
    try:
        f = open(kakao_send_log_FILE_PATH, 'a')
    except FileNotFoundError:
        return

    f.write(str(datetime.datetime.now()) + ": " + ent_name + "\n")
    f.close()


def record_error(code, api_status, func):
    try:
        f = open(error_log_FILE_PATH, 'a')
    except FileNotFoundError:
        return

    if code == 1:
        msg = "Date overflow in "
    elif code == 2:
        msg = "File open error in "
    elif code == 3:
        msg = str(api_status) + ": Post API failed in "
    elif code == 4:
        msg = str(api_status) + ": Get API failed in "
    elif code == 5:
        msg = "Access token expired in "

    f.write(str(datetime.datetime.now()) + ": " + msg + func + "\n")
    f.close()
