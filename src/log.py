import datetime


kakao_send_log_FILE_PATH = '/home/kmkim/Projects/git/kmkim036/Stock-Alarm/log/kakao_send.log'
error_log_FILE_PATH = '/home/kmkim/Projects/git/kmkim036/Stock-Alarm/log/error.log'
mail_send_log_FILE_PATH = '/home/kmkim/Projects/git/kmkim036/Stock-Alarm/log/mail_send.log'


def record_mail_send(ent_name):
    try:
        f = open(mail_send_log_FILE_PATH, 'a')
    except FileNotFoundError:
        return -1

    f.write(str(datetime.datetime.now()) + ": " + ent_name + "\n")
    f.close()


def record_kakao_send(ent_name):
    try:
        f = open(kakao_send_log_FILE_PATH, 'a')
    except FileNotFoundError:
        return -1

    f.write(str(datetime.datetime.now()) + ": " + ent_name + "\n")
    f.close()


def record_error(msg, func):
    try:
        f = open(error_log_FILE_PATH, 'a')
    except FileNotFoundError:
        return -1

    f.write(str(datetime.datetime.now()) + ": " + msg + " IN " + func + "\n")
    f.close()
