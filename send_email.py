import os
import re

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr, parseaddr

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    

smtp = smtplib.SMTP()
smtp.connect("smtp.163.com", port=25)
smtp.login(user="18539043730@163.com", password="EOWSDJSDWWRDFDRW")  # noqa


message = MIMEText('send_content', 'plain', 'utf-8')

sender = "agent<18539043730@163.com>"
message['From'] = _format_addr(sender)

receivers = ["recv<menglinhao@n6delta.com>"]
message['To'] = ','.join(list(map(_format_addr, receivers)))

message['Subject'] = Header('agent test failed notify.', 'utf-8')  # 定义主题内容

smtp.sendmail(from_addr="18539043730@163.com", to_addrs="menglinhao@n6delta.com", msg=message.as_string())
print('send successfully')