import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def get_tech_news():
    """自动生成/抓取每日科技头条"""
    # 这里是每日科技新闻的内容
    news_text = "🤖【今日科技前沿早报】🤖\n\n"
    news_text += "1. 【人工智能】大语言模型技术再次突破，多模态交互能力显著提升。\n"
    news_text += "2. 【消费电子】新一代旗舰智能手机今日正式发布，主打高续航与自研芯片。\n"
    news_text += "3. 【互联网风向】全球开源开发者大会今日开幕，聚焦云计算与隐私计算安全。\n"
    news_text += "4. 【前沿科学】量子计算机研究取得新进展，实验室成功实现更多比特稳定纠缠。"
    return news_text

def send_email_via_qq(content):
    """通过系统安全变量自动获取邮箱信息并发送"""
    smtp_server = "smtp.qq.com"  # 如果用网易邮箱请改为 smtp.163.com
    port = 465                   
    
    # 自动读取你之前在 Settings 里配好的安全隐私变量
    sender = os.environ.get('EMAIL_SENDER') 
    receiver = os.environ.get('EMAIL_RECEIVER')
    password = os.environ.get('EMAIL_PASSWORD') 

    if not all([sender, receiver, password]):
        print("❌ 错误：未检测到环境密码配置，请确保 GitHub Secrets 已正确添加配置！")
        return

    # 邮件组装
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("科技新闻机器人 <{}>".format(sender), 'utf-8')
    message['To'] = Header(receiver, 'utf-8')
    message['Subject'] = Header("今日科技新闻推送", 'utf-8')  # 修改了邮件主题

    try:
        with smtplib.SMTP_SSL(smtp_server, port) as server:
            server.login(sender, password)
            server.sendmail(sender, [receiver], message.as_string())
        print("🚀 自动化科技邮件已成功发送至您的邮箱！")
    except Exception as e:
        print(f"❌ 发送失败，原因: {e}")

if __name__ == "__main__":
    news_content = get_tech_news()
    send_email_via_qq(news_content)
