import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def get_news():
    """自动生成/抓取新闻内容"""
    news_text = "【今日股市早报】\n"
    news_text += "1. 今日大盘开盘小幅上扬，科技股领涨。\n"
    news_text += "2. 财经热点：量化交易新规出台，市场情绪回暖。\n"
    news_text += "3. 今日关注：多只大盘股今日公布财报。"
    return news_text

def send_email_via_qq(content):
    """通过邮箱自动发信"""
    smtp_server = "smtp.qq.com"  # 如果用网易邮箱就改 smtp.163.com
    port = 465                   
    
    # 填入你的邮箱和授权码（也可以在 GitHub Secrets 里配置）
    sender = "你的发件邮箱@qq.com" 
    receiver = "你的收件邮箱@qq.com"
    password = "你的16位邮箱授权码" 

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("新闻自动化机器人", 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header("今日股市新闻推送", 'utf-8')

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender, password)
            server.sendmail(sender, [receiver], message.as_string())
        print("🚀 自动化邮件发送成功！")
    except Exception as e:
        print(f"❌ 发送失败，原因: {e}")

if __name__ == "__main__":
    news_content = get_news()
    send_email_via_qq(news_content)
