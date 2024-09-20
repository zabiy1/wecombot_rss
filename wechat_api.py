import requests

# 企业微信机器人 webhook URL
WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=your_bot_key"

def send_to_wechat(content):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        }
    }
    response = requests.post(WEBHOOK_URL, headers=headers, json=data)
    if response.status_code == 200:
        print("消息推送成功")
    else:
        print(f"消息推送失败: {response.status_code} - {response.text}")
