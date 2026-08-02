import requests

WEBHOOK_URL = "ここにコピーしたウェブフックURLを貼り付け"

def send_discord_message(message):
    data = {
        "content": message
    }
    
    response = requests.post(WEBHOOK_URL, json=data)
    
    if response.status_code == 204:
        print("Discordへの送信に成功")
    else:
        print(f"送信失敗 (ステータスコード: {response.status_code})")

if __name__ == "__main__":
    send_message = "Pythonからのテストメッセージ"
    send_discord_message(send_message)