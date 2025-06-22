#app.py
import requests

# チャネルアクセストークン（長期）
access_token = 'YOUR_CHANNEL_ACCESS_TOKEN'

# あなたのユーザーID 
user_id = 'USER_ID'

# 送信したいメッセージ
messageText = 'ここにメッセージを入力してください'

# ヘッダー設定
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# メッセージ内容
data = {
    'to': user_id,
    'messages': [
        {
            'type': 'text',
            'text': messageText
        }
    ]
}

# LINE Messaging APIエンドポイント
url = 'https://api.line.me/v2/bot/message/push'

# メッセージ送信
response = requests.post(url, headers=headers, json=data)

# ステータスを確認
if response.status_code == 200:
    print('メッセージが送信されました' , messageText)
else:
    print(f'エラーが発生しました: {response.status_code}, {response.text}')