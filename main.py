import smtplib, requests
from email.mime.text import MIMEText

#     smtp.connect('smtp.qq.com', 587)

mail_host = "smtp.qq.com"
mail_user = '1445492109@qq.com'
mail_pass = "snckchglvhzsfhga"

sender = '1445492109@qq.com'
receivers = ['3160104943@zju.edu.cn']




# 获取天气
def getWhether(city, link):
    url = link + city
    r = requests.get(url).json()
    msg = '\r\n笨蛋，今日天气是' + r['data']['forecast'][0]['type'] + '\r\n温度:' + r['data']['forecast'][0]['high'] + '--' + \
          r['data']['forecast'][0]['low'] + '\r\n风：' + r['data']['forecast'][0]['fengli'][9:-3] + '--' + \
          r['data']['forecast'][0]['fengxiang'] + '\r\n\r\n' + r['data']['ganmao'] + '\r\n'
    return str(msg)


# 获取每日一句话
def getWord(link):
    r = requests.get(link).json()
    msg = '\r\n\r\n' + r['content'] + ' \r\n' + r['note']
    return str(msg)


# 一些用到的数据
data = {
    'link': 'http://open.iciba.com/dsapi/',
    'link2': 'http://wthrcdn.etouch.cn/weather_mini?city=',
    'city': '成都',
    'first': '早安小助手，上线啦!\r\n',
    'last': '\r\n\r\n                                       ——大头~'
}

# 构造邮件的文本数据
msg = data['first'] + getWhether(data['city'], data['link2']) + getWord(data['link']) + data['last']
message = """From: From Person <cs_zju@zju.edu.cn>
To: To Person <3160104943@zju.edu.cn>

This is a  e-mail message.
""" + msg


title = '笨蛋。请点击查收！'
content = message



def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件已发送！")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    sendEmail()
